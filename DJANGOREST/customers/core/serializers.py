from .models import Customer, Profession, DataSheet, Document
from rest_framework import serializers

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'dtype', 'doc_number', 'customer']

class DocumentSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'dtype', 'doc_number', 'customer']
        read_only_fields = ['customer']

class DataSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSheet
        fields = ['id', 'description', 'historial_data']

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['id', 'description', 'status']    

class CustomerSerializer(serializers.ModelSerializer):
    num_professions = serializers.SerializerMethodField()
    #data_sheet = serializers.StringRelatedField()
    #data_sheet = serializers.SerializerMethodField()
    #data_sheet = serializers.PrimaryKeyRelatedField(read_only=True)
    data_sheet = DataSheetSerializer()
    #professions = serializers.StringRelatedField(many=True)
    professions = ProfessionSerializer(many=True)
    document_set = DocumentSerializerCreate(many=True)
    
    class Meta:
        model = Customer
        fields = [
            'id', 'name', 'address', 'professions',
            'data_sheet', 'active', 'doc_num', 'status_message',
            'num_professions', 'document_set']
    
    def create(self, validated_data):
        professions = validated_data['professions']
        del validated_data['professions']

        document_set = validated_data['document_set']
        del validated_data['document_set']

        data_sheet = validated_data['data_sheet']
        del validated_data['data_sheet']
        
        d_sheet = DataSheet.objects.create(**data_sheet)
        customer = Customer.objects.create(**validated_data)
        customer.data_sheet = d_sheet

        for doc in document_set:
            Document.objects.create(
                dtype = doc['dtype'],
                doc_number=doc['doc_number'],
                customer_id = customer.id
            )

        for profession in professions:
            prof = Profession.objects.create(**profession)
            customer.professions.add(prof)
        
        return customer

    def get_num_professions(self, obj):
        return obj.num_professions()

    #def get_data_sheet(self, obj):
    #    return obj.data_sheet.description





