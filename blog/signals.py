from django.contrib.auth.models import Group,Permission

def create_group_permissions(sender, **kwargs):
    
    try:
        # Groups
        readers_group,created = Group.objects.get_or_create(name = "Readers")
        authors_group,created = Group.objects.get_or_create(name = "Authors")
        editors_group,created = Group.objects.get_or_create(name = "Editors")
        
        # Permissions
        reader_permissions = [
            Permission.objects.get(codename = "view_post")
        ]
        
        author_permissions = [
            Permission.objects.get(codename = "add_post"),
            Permission.objects.get(codename = "change_post"),
            Permission.objects.get(codename = "delete_post")
        ]
        publish_post,created = Permission.objects.get_or_create(codename = "publish_post",content_type_id = 8, name = "Can publish post")
        editor_permissions = [
            publish_post,
            Permission.objects.get(codename = "add_post"),
            Permission.objects.get(codename = "change_post"),
            Permission.objects.get(codename = "delete_post"),
        ]
        
        # Assigning
        readers_group.permissions.set(reader_permissions)
        authors_group.permissions.set(author_permissions)
        editors_group.permissions.set(editor_permissions)
        
        print("Groups & permissions Created Successfully")
        
    except Exception as e:
        print(f"An error occured {e}")
        
        