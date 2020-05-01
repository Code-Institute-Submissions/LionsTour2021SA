{% extends "base.html" %}
{% load static from staticfiles %}
{% load bootstrap_tags %}

{% block head_js %}
<script type="text/javascript" src="https://js.stripe.com/v2/"></script>
<script type="text/javascript">
    //<![CDATA[
        Stripe.publishableKey = '{{ publishable }}';
    //]]>
</script>
<script type="text/javascript" src="{% static 'js/stripe.js' %}"></script>
{% endblock %}

{% block content %}
<div class="row row-flex">
    {% for item in cart_items %}
        <div class="col-xs-10 col-xs-offset-1 col-sm-offset-0 col-sm-6 col-md-4 display panel panel-default">
            <div class="panel-body">
                <div class="product" style="background-image: url('{{ MEDIA_URL }}{{ item.product.image }}')"></div>

                <div class="caption">
                    <h3>{{ item.product.name }}</h3>
                    <p class="product-description">{{ item.product.descriptio }}</p>
                    <p>{{ item.quantity }}</p>
                    <p>item.product.price</p>
                </div>
            </div>
        </div>
    {% endfor %}
</div>
<div class="row">
    <p>Total</p>
    <p><span class="glyphicon glyphicon-euro" aria-hidden="true"></span>{{ total }}</p>
</div>

<form role="form" method="post" id="payment-form" action="{% url 'checkout' %}">
    <legend>Payment Details</legend>

    <div id="credit-card-errors" style="display: none;">
        <div class="alert-message block-message error" id="stripe-error-message"></div>
    </div>

    <div class="form-group col-md-6">
        {{ order_form | as_bootstrap }}
    </div>

    <div class="form-group col-md-6">
        {{ payment_form | as_bootstrap }}
    </div>

    {% csrf_token %}
    <div class="form-group col-md-12">
        <input class=" btn btn-primary" id="submit_payment_btn" name="commit" type="submit" value="Submit Payment">
    </div>
</form>
{% endblock %}