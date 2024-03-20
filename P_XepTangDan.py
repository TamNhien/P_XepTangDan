# Nhập vào ba số a, b, c và chuyển chúng thành kiểu float
a, b, c = map(float, input("Nhập ba số a, b, c: ").split())

# Sắp xếp ba số theo thứ tự tăng dần và lưu kết quả vào biến sorted_numbers
sorted_numbers = sorted([a, b, c])

# In ra ba số đã sắp xếp theo thứ tự tăng dần, sử dụng unpacking để in ra từng số một
print("Ba số đã sắp xếp theo thứ tự tăng dần:", *sorted_numbers)

