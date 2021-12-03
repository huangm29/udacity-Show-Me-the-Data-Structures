class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group): 
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user == "":
        print("Warning! Your searched user name is empty.")
        return False
    group_users = group.get_users()
    subgroup_list = group.get_groups()
    if user in group_users:
        return True
    elif len(subgroup_list)!=0:
        for subgroup in subgroup_list:
            if is_user_in_group(user,subgroup):
                return True 
    return False

#Test 1
print("\n Test 1")
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group(sub_child_user, parent)) 
#True

print("\n Test 2")
#Test 2 Empty case
print(is_user_in_group("", parent))
#Warning! Your searched user name is empty
#False

#Test 3 
print("\n Test 3")
group_1 = Group("1")
group_2  = Group("2")

group_2.add_user("user")

group_1.add_group(group_2)
group_2.add_group(group_1)

print(is_user_in_group("user", group_1))
#True

print(is_user_in_group("users", group_1))
#RecursionError: maximum recursion depth exceeded in comparison