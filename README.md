# Ứng dụng Chat Bảo mật với Mã hóa AES

Dự án này trình bày một ứng dụng chat cơ bản với mã hóa đầu cuối (E2EE) sử dụng AES (Advanced Encryption Standard). Hệ thống bao gồm một máy chủ và nhiều máy khách có thể gửi và nhận tin nhắn được mã hóa, đảm bảo rằng nội dung chỉ có thể được đọc bởi người nhận dự định.

## Tính năng
- Mã hóa đầu cuối sử dụng AES.
- Hỗ trợ nhiều máy khách với một máy chủ trung tâm.
- Nhận diện tên người dùng cho mỗi máy khách.
- Tin nhắn được mã hóa và giải mã phía máy khách.
- Giao diện người dùng đơn giản để gửi và nhận tin nhắn.

## Yêu cầu

Đảm bảo bạn đã cài đặt các phần mềm sau:
- Cài đặt VSCode
- Python 3.6+
- Virtualenv (tuỳ chọn nhưng được khuyến nghị)
- Cài đặt các Extension của Python

## Cài đặt

1. **Thiết lập môi trường ảo:**
   ```sh
   python -m venv venv
# Trên Mac , sử dụng source venv/bin/activate  

# Trên Windows, sử dụng `venv\Scripts\activate`

2. **Cài đặt các thư viện cần thiết:**
    pip install pycryptodome

## Sử dụng
1. **Khởi động Máy chủ**
Điều hướng tới thư mục dự án và chạy máy chủ:
    python server.py
    Máy chủ sẽ bắt đầu và lắng nghe các kết nối đến trên localhost:9999.

2. **Khởi động Máy khách**
Mở một cửa sổ terminal mới, điều hướng tới thư mục dự án và chạy máy khách:
    python client.py
Như vậy sẽ khởi tạo được một máy khách

## Lưu ý
Cần khởi tạo máy chủ trước để máy chủ running rồi tạo các máy khách để thực hiện giao tiếp