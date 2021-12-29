from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from .models import *

"""
adminpanel views
1. Create 
2. update
3. delete 
Operation for all the models
"""



""" 
creat, read, update, delete operation Currecy
"""

class CurrencyGET(View):
    def get(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            crs = Currency.objects.filter(
                shop=shopId.id
            )

            args = {
                "crs": crs
            }
            return render(request, "", args)
        else:
            return redirect("warning")


class CurrencyPOST(View):
    def get(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            args = {}
            return render(request, "adminpanel/currency/create-currency.html", args)

    def post(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            if request.method == "POST":
                currency_sign = request.POST.get("currency_sign")

                currency = Currency(
                    currency_sign=currency_sign
                )

                currency.save()
                return redirect(f"")
        else:
            return redirect("warning")

class CurrencyPUT(View):
    def get(self, request, shop_id, id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        cr_id = get_object_or_404(Currency, pk=id)
        if shopId.user == request.user:
            args = {"cr_id": cr_id,}
            return render(request, "adminpanel/currency/edit-currency.html", args)
        else:
            return redirect("warning")
    
    def post(self, request, shop_id, id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        cr_obj = get_object_or_404(Currency, pk=id)
        if shopId.user == request.user:
            if request.method == "POST":
                cr_obj.currency_sign = request.POST.get("currency_sign")
                cr_obj.save()
                return redirect(f"")
        else:
            return redirect("")

            

class CurrencyDELETE(View):
    def post(self, request, shop_id, id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        cr_obj = get_object_or_404(Currency, pk=id)
        if shopId.user == request.user:
            if request.method == "POST":
                cr_obj.delete()
                return redirect(f"")
        else:
            return redirect("")



"""
Create, GET, update, delete for Shop
"""

class ShopOperation(models.Model):
    def get(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            args = {
                "shopId": shopId,
            }
            return render(request, "", args)
        else:
            return redirect("warning")

class ShopPOST(View):
    def get(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            args = {}
            return render(request, "adminpanel/shop/create-shop.html", args)
    def post(self, request, shop_id):
        pass

class ShopPUT(View):
    def get(self, request, shop_id, id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            args = {}
            return render(request, "adminpanel/shop/edit-shop.html", args)
        else:
            return redirect("warning")

    def post(self, request, shop_id, id):
        pass


class ShopDELETE(View):
    def delete(self, request, shop_id, id):
        pass
    
"""
POST, GET, PUT, DELETE for Brand
"""

class BrandGET(View):
    def get(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            brands = GrocerryBrand.objects.filter(
                shop=shopId.id
            )
            args = {
                "shopId": shopId,
                "brands": brands,
            }
            return render(request, "", args)
        else:
            return redirect("warning")

    def post(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            if request.method == "POST":
                post = request.POST
                brand_title = post.get("brand_title")
                brand_logo = request.FILES.get("brand_logo")

                if brand_title and brand_logo:
                    brand = GrocerryBrand(
                        shop=shopId.id,
                        brand_title=brand_title,
                        brand_logo=brand_logo
                    )
                    brand.save()
                    return redirect(f"")
                else:
                    brand = GrocerryBrand(
                        brand_title
                    )
                    brand.save()
                    return redirect(f"")


class BrandPUT(View):
    def get(self, request, shop_id, id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        brand_obj = get_object_or_404(GrocerryBrand, pk=id)
        if shopId.user == request.user:
            args = {
                "shopId": shopId,
                "brand_obj": brand_obj,
            }
            return render(request, "adminpanel/brand/edit-brand.html", args)
    def put(self, request, shop_id, id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        brand_obj = get_object_or_404(GrocerryBrand, pk=id)
        if shopId.user == request.user:
            if request.method == "POST":
                if brand_obj is not None and brand_obj.brand_logo is None:
                    brand_obj.brand_title = request.POST.get("brand_title")
                    brand_obj.save()

                    return redirect(f"")
                else:
                    brand_obj.brand_title = request.POST.get("brand_title")
                    brand_obj.brand_logo = request.FILESS.get("brand_logo")
                    brand_obj.save()

                    return redirect(f"")


class BrandDELETE(View):
    def post(self, request, shop_id, id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        brand_obj = get_object_or_404(GrocerryBrand, pk=id)
        if shopId.user == request.user:
            if brand_obj is not None:
                brand_obj.delete()
                return redirect(f"")
        else:
            return redirect("")


"""
GET, POST, PUT, DELETE operation for Category
"""

class CategoryOperation(View):
    def get(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            cats = GrocerryCategory.objects.filter(
                shop=shopId.id
            )
            args = {
                "cats": cats,
                "shopId": shopId,
            }
            return render(request, "adminpanel/category/category.html", args)
        else:
            return redirect("warning")


    def post(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            if request.method == "POST":
                category_title = request.POST.get("category_title")

                category = GrocerryCategory(
                    category_title=category_title
                )

                category.save()
                return redirect(f"")
        else:
            return redirect("warning")

    def update_category(self, request, shop_id, id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        cat_obj = get_object_or_404(GrocerryCategory, pk=id)
        if shopId.user == request.user:
            if request.method == "PUT":
                cat_obj.category_title = request.POST.get("category_title")
                cat_obj.save()
                return redirect(f"")
            args = {
                "shopId": shopId,
                "cat_obj": cat_obj,
            }
            return render(request, "adminpanel/category/edit-category.html", args)
        else:
            return redirect("")

    def delete(self, request, shop_id, id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        cat_obj = get_object_or_404(GrocerryCategory, pk=id)
        if shopId.user == request.user:
            if request.method == "POST":
                cat_obj.delete()
                return redirect(f"")
        else:
            return redirect("")


"""
GET, POST, PUT, DELETE for ROLES
"""

class RoleOperation(View):
    def get(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            roles = Roles.objects.filter(
                shop=shopId.id
            )

            args = {
                "roles": roles,
            }

            return render(request, "", args)
        
        else:
            return redirect("")


    def post(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            if request.method == "POST":
                post = request.POST
                role_title = post.get("role_title")
                is_admin = post.get("is_admin")
                can_config_pos = post.get("can_config_pos")
                can_config_roles = post.get("can_config_roles")
                can_config_orders = post.get("can_config_orders")
                can_config_inventory = post.get("can_config_inventory")
                can_config_customers = post.get("can_config_customers")
                can_config_vendors = post.get("can_inventory_vendors")
                can_config_tables = post.get("can_config_tables")
                can_config_emps = post.get("can_config_emps")
                can_manage_settings = post.get("can_manage.settings")


                roles = Roles(
                    role_title = role_title,
                    is_admin = is_admin,
                    can_config_pos = can_config_pos,
                    can_config_roles = can_config_roles,
                    can_config_orders = can_config_orders,
                    can_config_inventory = can_config_inventory,
                    can_config_customers = can_config_customers,
                    can_config_vendors = can_config_vendors,
                    can_config_tables = can_config_tables,
                    can_config_emps = can_config_emps,
                    can_manage_settings = can_manage_settings,
                )

                roles.save()
                return redirect(f"")
        else:
            return redirect("")

    
    def put(self, request, shop_id, id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        role_obj = get_object_or_404(Roles, pk=id)

        if shopId.user == request.method:
            if request.method == "POST":
                role_obj.role_title = request.POST.get("role_title")
                role_obj.is_admin = request.POST.get("is_admin")
                role_obj.can_config_pos = request.POST.get("can_config_pos")
                role_obj.can_config_roles = request.POST.get("can_config_roles")
                role_obj.can_config_orders = request.POST.get("can_config_orderss")
                role_obj.can_config_inventory = request.POST.get("can_config_inventory")
                role_obj.can_config_customers = request.POST.get("can_config_customers")
                role_obj.can_config_vendors = request.POST.get("can_config_vendors")
                role_obj.can_config_tables = request.POST.get("can_config_tables")
                role_obj.can_config.emps = request.POST.get("can_config_emps")
                role_obj.can_manage_settings = request.POST.get("can_manage_settings")

                
                role_obj.save()
                return redirect(f"")
        else:
            return redirect("")


    def delete(self, request, shop_id, id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        role_obj = get_object_or_404(Roles, pk=id)
        if shopId.user == request.user:
            role_obj.delete()
            return redirect(f"")
        else:
            return redirect("")


"""
GET, POST, PUT, DELETE for Vendor
"""

class VendorOpeartion(View):
    def get(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)

        if shopId.user == request.user:
            vendors = Vendor.objects.filter(
                shop=shopId.id
            )
            args = {
                "vendors": vendors,
            }
            return render(request, "", args)
        else:
            return redirect("Warning")

    def post(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            pass

    def put(self, request, shop_id, id):
        pass

    def delete(self, request, shop_id, id):
        pass


class Exception404notFound(View):
    def get(self, request):
        message = "404 Not Found"
        args = {
            "message": message,
        }
        return render(request, "exceptions/warning.html")