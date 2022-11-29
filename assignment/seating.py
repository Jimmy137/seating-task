import string
#from turtle import Screen, Turtle

alphabet = list(string.ascii_lowercase)

def sorti(seat):
    seat_arr = seat['seat_name'].split('-')
    r = seat_arr[1]
    return int(r)
def seating(arrs,passengers):
    number_of_seats = 0
    packages = []
    

    for i,arr in enumerate(arrs):
        seats = arr[0] * arr[1]
        rows = arr[1]
        cols = arr[0]
        package_letter = alphabet[i]
        seats_names_and_passengers = []
        for r in range(rows):
            
            row_num = str(r+1)

            for c in range(cols):
                property= 'center'
                
                col_num = str(c+1)
                if c == 0:
                    property = 'aisle'
                    if i == 0:
                        property = 'window'
                if c + 1  == arr[0]:
                    property = 'aisle'
                    if i +1 == len(arrs):
                        property = 'window'

                seat_name = package_letter + '-' + col_num  + '-' + row_num + '-' + property
                passenger = ''

                seats_names_and_passengers.append({'name': seat_name , 'passenger':passenger})

        packages.append({'package': package_letter, 'seats': seats, 'seats_names': seats_names_and_passengers})
        
        number_of_seats += seats

    passengers_names = []
    for p in range(passengers):
        passengers_name = 'p' + '-' + str(p+1)
        passengers_names.append(passengers_name)
  

    all_seats = []
    for package in packages:
        for seat in package["seats_names"]:
            seat_name_org = seat['name']
            all_seats.append((seat_name_org))

    aisle_seats = []
    window_seats = []
    center_seats = []

    for seat in all_seats:
        if 'aisle' in seat:
            aisle_seats.append(seat)
        elif 'window' in seat:
            window_seats.append(seat)
        else:
            center_seats.append(seat)

    all_seats = aisle_seats + window_seats + center_seats
    all_seats_new = []

    for seat in all_seats:
        seat_name = ''
        seat_letter = seat.split('-')[0].strip()
        seat_package_col = int(seat.split('-')[1].strip())
        general_col = seat_package_col
        arr_idx = alphabet.index(seat_letter)
        if arr_idx != 0:       
            for j in range(arr_idx):
                general_col += arrs[j][0]
        str_seat_package_col = str(seat_package_col)
        seat_name = seat.replace(f'{seat_letter}-{str_seat_package_col}',str(general_col))   

        all_seats_new.append({'seat_name':seat_name,'serial':seat})

    aisle_seats_new = []
    window_seats_new = []
    center_seats_new = []   
    for seat in all_seats_new:
        if 'aisle' in seat['seat_name']:
            aisle_seats_new.append(seat)
        elif 'window' in seat['seat_name']:
            window_seats_new.append(seat)
        else:
            center_seats_new.append(seat)
    aisle_seats_new.sort(key=sorti)   
    window_seats_new.sort(key=sorti) 
    center_seats_new.sort(key=sorti) 
    all_seats_new = aisle_seats_new + window_seats_new + center_seats_new
    

    final_result = []
    for i,p in enumerate(passengers_names):
        seat = all_seats_new[i]
        final_result.append({'passenger': p, 'seat': seat})
    
        
    print(final_result)   

if __name__ == "__main__":
    raw_arr_rows_cols = input()
    p_count = int(input('Number of passengers:'))
    str_arr_r_c = raw_arr_rows_cols.replace('[','').replace(']','')
    arr_r_c = list(map(int, str_arr_r_c.split(',')))
    arr_of_arr_r_c = []
    
    for i in range(int(len(arr_r_c) / 2)):
        cols_idx = i * 2
        rows_idx = (i * 2) + 1
        rows = arr_r_c[rows_idx]
        cols = arr_r_c[cols_idx]
        arr_of_arr_r_c.append([cols, rows])
        
        
    seating(arr_of_arr_r_c, p_count)


