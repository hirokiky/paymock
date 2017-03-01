=======
paymock
=======

Mock library for `payjp <https://github.com/payjp/payjp-python/>`_.
paymock will completely mock the HTTP API of pay.jp, and payjp library will access the mocked API.

This library can be used with `responses <https://github.com/getsentry/responses/>`_

Usage
=====

Mocking API to create Subscription.

.. code-block:: python

    >>> from payment import paymock
    >>> subscription = paymock.factory_subscription("sub_xxx", current_period_end=1488357063)
    >>>
    >>> import responses
    >>>
    >>> with responses.mock:
    ...     paymock.mock_create(subscription)
    ...     import payjp
    ...     created = payjp.Subscription.create()
    ...
    2017-03-01 18:00:01,897 payjp INFO POST https://api.pay.jp/v1/subscriptions 200
    >>> created
    <PayjpObject id=sub_xxx at 0x1069dd958> JSON: {
      "current_period_end": 1488357063,
      "id": "sub_xxx"
    }

It means...

1. ``paymock.factory_subscription()``: Creating dummy Subscription object
2. ``with responses.mock``: Activating
3. ``paymock.mock_create()``: Mocking the create API for Subscription

  * The mocked API will return data for ``subscription`` you created

4. ``created = payjp.Subscription.create()``: Creating Subscription

  * This code won't access to ``api.pay.jp``.

5. ``created``: Created subscription is completely same with your mocking object

Also ``responses`` can be used as decorator, so it's useful on test methods.


.. code-block:: python

    import paymock
    import responses


    class TestYours(TestCase):
        @responses.activate
        def test_something(self):
            customer = paymock.factory_customer('cus_xxx')
            paymock.mock_get(customer)

            call_function_under_test()  # This function will access pay.jp to get Customer


Mocking list object
===================

.. code-block:: python

    customer = paymock.factory_customer(id='cus_xxx')
    card = paymock.factory_card(
        'car_xxx',
        customer,
        last4='4242',
        exp_month=8,
        exp_year=2020,
    )

    paymock.mock_create(customer)
    paymock.mock_create_list(customer.cards, card)


Mocking errors
==============

paymock can also mock error responses.
This code is to simulate creating Card returns ``token_already_used`` error.

.. code-block:: python

    customer = paymock.factory_customer('cus_xxx')

    paymock.mock_create(customer)
    paymock.mock_error(
        responses.POST, customer.cards.url,
        paymock.ERROR_TOKEN_ALREADY_USED,
    )
