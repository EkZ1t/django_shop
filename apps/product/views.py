from rest_framework import viewsets
from .models import Product 
from .permissions import IsOwner
from .serializers import ProductSerializer
from rest_framework import permissions 


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    seriazlier_class = ProductSerializer 
    
    def get_permissions(self):
        method = self.request.method
        if method in permissions.SAFE_METHODS:
            self.permission_classes = [permissions.AllowAny]
        elif method == 'POST':
            self.permission_classes = [permissions.IsAuthenticated]
        elif method in ['DELETE', 'PUT', 'PATCH']:
            self.permission_classes = [IsOwner]
        return super().get_permissions()