         
def Node(value):
    return{"value":value,"next":None}


def linked_list(value):
    new_node=Node(value=value)
    return {"head":new_node,"tail":new_node,"length":1}

def Print_linked_list(linked_list):
    current = linked_list["head"]
    all_value=[]
    for i in range(int(linked_list["length"])) :
        all_value.append(current["value"])
        current = current["next"]
    return all_value

def append_node(linked_list,value):
    new_node=Node(value=value)
    linked_list["tail"]["next"]=new_node
    linked_list["tail"]=new_node
    linked_list["length"]+=1 
    return linked_list

def pop_node(linked_list):
    if not linked_list:
        return 
    if linked_list["length"] == 1:
        return 
    current = linked_list["head"]
    for i in range(int(linked_list["length"])-2) :
        current = current["next"]
    current["next"]=None
    linked_list["length"]-=1
    linked_list["tail"]=current
    return linked_list

def prepend_node(linked_list,value):
    new_node=Node(value=value)
    if not linked_list:
        return {"head":new_node,"tail":new_node,"length":1}
    new_node["next"]=linked_list["head"]
    return {"head":new_node,"tail":linked_list["tail"],"length":int(linked_list["length"])+1}

def pop_first_node(linked_list):
    if not linked_list:
        return
    if linked_list["length"] ==1:
        return
    return {"head":linked_list["head"]["next"],"tail":linked_list["tail"],"length":linked_list["length"]-1}
    
def get_node_by_index(linked_list,index):
    if index < 0 or index > linked_list["length"]-1 :
        return
    current = linked_list["head"]
    for i in range(index) :
        current = current["next"]
    return current

def insert_new_node(linked_list,index,value):
    if index ==0:
        return prepend_node(linked_list,value)
    if index ==linked_list["length"]:
        return append_node(linked_list,value)
    new_node=Node(value=value)
    current = linked_list["head"]
    temp=current
    for i in range(index):
        if i < index-1:
            temp=current["next"]
        current = current["next"]
    temp["next"]=new_node
    temp["next"]["next"]=current
    linked_list["length"]+=1
    return linked_list

def update_node(linked_list,index,value):
    existing=get_node_by_index(linked_list,index)
    if not existing:
        return linked_list
    existing["value"]=value
    return linked_list

def remove_node_using_index(linked_list,index):
    if index ==0:
        return pop_first_node(linked_list)
    if index ==linked_list["length"]:
        return pop_node(linked_list)
    existing=get_node_by_index(linked_list,index-1)
    temp=existing["next"]["next"]
    existing["next"]=temp
    linked_list["length"]-=1
    return linked_list

def reverse_all_nodes(linked_list):
    prev = None
    current = linked_list["head"]
    
    linked_list["tail"] = current

    while current is not None:
        next_node = current["next"]
        current["next"] = prev
        prev = current
        current = next_node

    linked_list["head"] = prev

    return linked_list

my_linked_list = linked_list(4)

print("\n created new node")
print("----------------------------------------------")
print(my_linked_list)

my_linked_list=append_node(my_linked_list , 2)
my_linked_list=append_node(my_linked_list , 1)
my_linked_list=append_node(my_linked_list , 8)
my_linked_list=append_node(my_linked_list , 11)

print("\n appender node")
print("----------------------------------------------")
print(my_linked_list)



my_linked_list=pop_node(my_linked_list)

print("\n pop node")
print("----------------------------------------------")
print(my_linked_list)

my_linked_list=prepend_node(my_linked_list,5)

print("\n prepend new node")
print(my_linked_list)

my_linked_list=pop_first_node(my_linked_list)

print("\n pop first node")
print("----------------------------------------------")
print(my_linked_list)

my_linked_list=insert_new_node(my_linked_list,3,10)

print("\n insert new node")
print("----------------------------------------------")
print(my_linked_list)

my_linked_list=update_node(my_linked_list,1,5)

print("\n update node")
print("----------------------------------------------")
print(my_linked_list)


my_linked_list=remove_node_using_index(my_linked_list,1)

print("\n remove node using index")
print("----------------------------------------------")
print(my_linked_list)

my_linked_list=reverse_all_nodes(my_linked_list)

print("\n reversed nodes")
print("----------------------------------------------")
print(my_linked_list)






print("\n----------------------------------------------\n")

print(Print_linked_list(my_linked_list))

print("\n----------------------------------------------\n")

print(get_node_by_index(my_linked_list,0)["value"])