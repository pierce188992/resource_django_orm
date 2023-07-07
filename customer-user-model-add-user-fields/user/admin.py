from django.contrib import admin

from user.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

# 將userprofile 內連到 admin的user介面
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

# 新增user時 admin介面不會出現 userprofile
class AccountsUserAdmin(AuthUserAdmin):
    def add_view(self, *args, **kwargs):
        self.inlines =[]
        return super(AccountsUserAdmin, self).add_view(*args, **kwargs)
        
# 改變user時 admin介面會出現 userprofile
    def change_view(self, *args, **kwargs):
        self.inlines =[UserProfileInline]
        return super(AccountsUserAdmin, self).change_view(*args, **kwargs)


admin.site.unregister(User)
admin.site.register(User, AccountsUserAdmin)
