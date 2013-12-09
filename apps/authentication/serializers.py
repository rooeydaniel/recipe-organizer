#from rest_framework import serializers
#
#from .models import User
#from apps.recipe.models import Recipe
#
#
#class UserSerializer(serializers.ModelSerializer):
#    recipes = serializers.HyperlinkedIdentityField('recipes', view_name='recipe-list', lookup_field='username')
#
#    class Meta:
#        model = User
#        fields = ('id', 'username', 'email', 'gender', 'recipes', )