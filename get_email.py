import get_data

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    list1=[]
    results=data['results']
    for i in results:
        list1.append(i['email'])
    return list1
x=get_data.get_data('randomuser_data.json')
print(get_email(x))