import json
import os
from urllib.parse import urljoin

import payjp
from payjp.resource import Card
import responses

DUMMY_KEY = 'dummy_key'


def factory_customer(id, **kwargs):
    cards = {
        "count": 0,
        "data": [],
        "has_more": False,
        "object": "list",
        "url": "/v1/customers/" + id + "/cards"
    }
    data = kwargs.copy()
    data['id'] = id
    data['object'] = 'customer'
    data['cards'] = cards
    customer = payjp.Customer.construct_from(
        data, DUMMY_KEY
    )
    return customer


def factory_card(id, customer, **kwargs):
    d = kwargs.copy()
    d['id'] = id
    d['object'] = 'card'
    d['customer'] = customer.id
    card = Card.construct_from(d, DUMMY_KEY)
    return card


def factory_subscription(id, **kwargs):
    d = kwargs.copy()
    d['id'] = id
    subscription = payjp.Subscription.construct_from(d, DUMMY_KEY)
    return subscription


def mock_get(payobj):
    url = urljoin(payjp.api_base, payobj.instance_url())
    responses.add(
        responses.GET, url,
        body=json.dumps(payobj), status=200,
        content_type='application/json',
    )


def mock_create(payobj):
    url = urljoin(payjp.api_base, payobj.class_url())
    responses.add(
        responses.POST, url,
        body=json.dumps(payobj), status=200,
        content_type='application/json',
    )


def mock_update(payobj):
    url = urljoin(payjp.api_base, payobj.instance_url())
    responses.add(
        responses.POST, url,
        body=json.dumps(payobj), status=200,
        content_type='application/json',
    )


def mock_delete(payobj):
    url = urljoin(payjp.api_base, payobj.instance_url())
    body = json.dumps({
        "deleted": True,
        "id": payobj.id,
        "livemode": False
    })
    responses.add(
        responses.DELETE, url,
        body=body, status=204,
        content_type='application/json',
    )


def mock_get_list(list_obj, payobj):
    url = urljoin(payjp.api_base, os.path.join(list_obj.url, payobj.id))
    responses.add(
        responses.GET, url,
        body=json.dumps(payobj), status=200,
        content_type='application/json',
    )


def mock_create_list(list_obj, payobj):
    url = urljoin(payjp.api_base, list_obj.url)
    responses.add(
        responses.POST, url,
        body=json.dumps(payobj), status=200,
        content_type='application/json',
    )


ERROR_BASE = {
  "error": {
    "code": "invalid_param_key",
    "message": "",
    "param": "",
    "status": 400,
    "type": "client_error"
  }
}

ERROR_INVALID_NUMBER = "invalid_number"
ERROR_INVALID_CVC = "invalid_cvc"
ERROR_INVALID_EXPIRY_MONTH = "invalid_expiry_month"
ERROR_INVALID_EXPIRY_YEAR = "invalid_expiry_year"
ERROR_EXPIRED_CARD = "expired_card"
ERROR_CARD_DECLINED = "card_declined"
ERROR_PROCESSING_ERROR = "processing_error"
ERROR_MISSING_CARD = "missing_card"
ERROR_INVALID_ID = "invalid_id"
ERROR_NO_API_KEY = "no_api_key"
ERROR_INVALID_API_KEY = "invalid_api_key"
ERROR_INVALID_PLAN = "invalid_plan"
ERROR_INVALID_EXPIRY_DAYS = "invalid_expiry_days"
ERROR_UNNECESSARY_EXPIRY_DAYS = "unnecessary_expiry_days"
ERROR_INVALID_FLEXIBLE_ID = "invalid_flexible_id"
ERROR_INVALID_TIMESTAMP = "invalid_timestamp"
ERROR_INVALID_TRIAL_END = "invalid_trial_end"
ERROR_INVALID_STRING_LENGTH = "invalid_string_length"
ERROR_INVALID_COUNTRY = "invalid_country"
ERROR_INVALID_CURRENCY = "invalid_currency"
ERROR_INVALID_ADDRESS_ZIP = "invalid_address_zip"
ERROR_INVALID_AMOUNT = "invalid_amount"
ERROR_INVALID_PLAN_amoUNT = "invalid_plan_amount"
ERROR_INVALID_CARD = "invalid_card"
ERROR_INVALID_CUSTOMER = "invalid_customer"
ERROR_INVALID_BOOLEAN = "invalid_boolean"
ERROR_INVALID_EMAIL = "invalid_email"
ERROR_NO_ALLOWED_PARAM = "no_allowed_param"
ERROR_NO_PARAM = "no_param"
ERROR_INVALID_QUERYSTRING = "invalid_querystring"
ERROR_MISSING_PARAM = "missing_param"
ERROR_INVALID_PARAM_KEY = "invalid_param_key"
ERROR_NO_PAYMENT_METHOD = "no_payment_method"
ERROR_PAYMENT_METHOD_DUPLICATE = "payment_method_duplicate"
ERROR_PAYMENT_METHOD_DUPLICATE_INCLUDING_CUSTOMER = "payment_method_duplicate_including_CUSTOMER"
ERROR_FAILED_PAYMENT = "failed_payment"
ERROR_INVALID_REFUND_AMOUNT = "invalid_refund_amount"
ERROR_ALREADY_REFUNDED = "already_refunded"
ERROR_CANNOT_REFUND_BY_AMOUNT = "cannot_refund_by_amount"
ERROR_INVALID_AMOUNT_TO_NOT_CAPTURED = "invalid_amount_to_not_captured"
ERROR_REFUND_AMOUNT_GT_NET = "refund_amount_gt_net"
ERROR_CAPTURE_AMOUNT_GT_NET = "capture_amount_gt_net"
ERROR_INVALID_REFUND_REASON = "invalid_refund_reason"
ERROR_ALREADY_CAPTURED = "already_captured"
ERROR_CANT_CAPTURE_REFUNDED_CHARGE = "cant_capture_refunded_charge"
ERROR_CHARGE_EXPIRED = "charge_expired"
ERROR_ALERADY_EXIST_ID = "alerady_exist_id"
ERROR_TOKEN_ALREADY_USED = "token_already_used"
ERROR_ALREADY_HAVE_CARD = "already_have_card"
ERROR_DONT_HAS_THIS_CARD = "dont_has_this_card"
ERROR_DOESNT_HAVE_CARD = "doesnt_have_card"
ERROR_INVALID_INTERVAL = "invalid_interval"
ERROR_INVALID_TRIAL_DAYS = "invalid_trial_days"
ERROR_INVALID_BILLING_DAY = "invalid_billing_day"
ERROR_EXIST_SUBSCRIBERS = "exist_subscribers"
ERROR_ALREADY_SUBSCRIBED = "already_subscribed"
ERROR_ALREADY_CANCELED = "already_canceled"
ERROR_ALREADY_PASUED = "already_pasued"
ERROR_SUBSCRIPTION_WORKED = "subscription_worked"
ERROR_TEST_CARD_on_LIVEMODE = "test_card_on_livemode"
ERROR_NOT_ACTIVATED_ACCOUNT = "not_activated_account"
ERROR_TOO_MANY_TEST_REQUEST = "too_many_test_request"
ERROR_INVALID_ACCESS = "invalid_access"
ERROR_PAYJP_WRONG = "payjp_wrong"
ERROR_PG_WRONG = "pg_wrong"
ERROR_NOT_FOUND = "not_found"
ERROR_NOT_ALLOWED_METHOD = "not_allowed_method"


def mock_error(method, path, code, status=400):
    err = ERROR_BASE.copy()
    err['code'] = code
    err['status'] = status
    url = urljoin(payjp.api_base, path)
    responses.add(
        method, url, body=json.dumps(err),
        status=status, content_type='application/json'
    )
