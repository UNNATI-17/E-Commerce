from django.contrib import admin

# Register your models here.
from core.models import ProductReview, Product, Category,Vendor, CartOrder, CartOrderItems, ProductImages, wishlists, Address

class ProductImageAdmin(admin.TabularInline):
    model = ProductImages
    extra = 1  # Show one empty form by default
    fields = ['images', 'date']  # Only show these two fields
    readonly_fields = ['date']  # Make date uneditable

class ProductAdmin(admin.ModelAdmin):
    list_display = ['user','title','product_image', 'price', 'category','vendor', 'featured','product_status']
    inlines = [ProductImageAdmin]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','category_image']

class VendorAdmin(admin.ModelAdmin):
    list_display = ['title','vendor_image']


class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user','price','paid_status','order_date','product_status']

class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order','invoice_number','item','image','qty','product_status','price']
    
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user','product','review','rating']

class wishlistadmin(admin.ModelAdmin):
    list_display = ['user','product','date']

class AddressAdmin(admin.ModelAdmin):
    list_display = ['user','address','status']

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)


admin.site.register(Vendor,VendorAdmin)
admin.site.register(CartOrder,CartOrderAdmin)
admin.site.register(CartOrderItems,CartOrderItemsAdmin)
admin.site.register(ProductReview,ProductReviewAdmin)
admin.site.register(wishlists,wishlistadmin)
admin.site.register(Address,AddressAdmin)







