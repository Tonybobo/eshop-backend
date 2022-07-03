from mongoengine import Document, EmbeddedDocument, fields


# Create your models here.

class Games(Document):

    title = fields.StringField()
    description = fields.StringField(null=True)
    imageUrl = fields.StringField(null=True)
    store = fields.DictField()
    msrp =  fields.DictField()
    publishers = fields.StringField(null=True)
    releaseDate = fields.DateTimeField()
    class Meta:
        ordering = ['title']
        db_table = "games"
    
   
    
class Currency(Document):
    _id = fields.ObjectIdField() 
    id = fields.StringField()
    rate = fields.DecimalField(max_digits=10 , decimal_places= 5)
    class Meta:
        db_table = "currency"
    