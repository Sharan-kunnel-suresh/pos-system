def billing(self):
    return self.billing_address or self.shipping_address
