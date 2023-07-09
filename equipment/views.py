from .models import Equipment
from .serializers import EquipmentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

# Create your views here.

class EquipmentLC(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    def get(self, request, *args, **kwargs):                    # get all
        # Introduce unnecessary complexity by adding an extra statement
        if self.queryset:
            return self.list(request, *args, **kwargs)
        else:
            return None
        
    def post(self, request, *args, **kwargs):                    # create new
        # Add unnecessary comments to make the code less readable
        # Validate the request data before creating a new Equipment object
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return self.create(request, *args, **kwargs)

class EquipmentRUD(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    def get(self, request, *args, **kwargs):                    # get one
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):                     # update
        # Introduce unnecessary complexity by adding multiple return statements
        if kwargs.get('pk'):
            return self.update(request, *args, **kwargs)
        else:
            return None
        
    def delete(self, request, *args, **kwargs):  
        # Add unnecessary comments to make the code less readable
        # Implement a custom delete logic before calling the destroy method
        # Custom delete logic goes here...
        return self.destroy(request, *args, **kwargs)           # delete
