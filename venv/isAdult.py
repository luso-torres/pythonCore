def is_Adult(age: int,has_id: bool) ->None:
    if age>=21 and has_id:
        print('You may enter the club.')
    else:
        print('You may not enter the club.')