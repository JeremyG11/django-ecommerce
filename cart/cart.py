

class Cart():
    
    def __init__(self,request):
        
        self.session = request.session
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        self.cart = cart
        
            
    def add(self, product):
        
        product_id = product.id;
        
        if product_id not in self.cart:
            self.cart[product_id] = str({'price': product.price})
            
        self.session.modified = True