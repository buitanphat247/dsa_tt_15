# Chuyên Đề: Cấu Trúc Dữ Liệu Chuyên Biệt (Trie & Union-Find)
### *Tối Ưu Hóa Truy Vấn Chuỗi Tiền Tố & Quản Lý Tập Hợp Rời Rạc Trong Hệ Thống Hiệu Năng Cao*

---

## 👥 Thông Tin Chuyên Đề & Nhóm Nghiên Cứu
- **Môn học:** Cấu trúc Dữ liệu & Giải thuật (Data Structures & Algorithms)
- **Lớp / Mã nhóm:** `DASA230179_06`
- **Giảng viên hướng dẫn:** Thầy Vũ Đình Bảo (T-Bao)
- **Danh sách thành viên:**
  1. **Lê Thị Tuyết Nhi** (MSSV: 25110283) — *Phần I: Đặt vấn đề & Cấu trúc Trie*
  2. **Mai Thanh Trà** (MSSV: 25110372) — *Phần II: Cấu trúc Union-Find (DSU) & Kruskal*
  3. **Huỳnh Thị Thùy Trang** (MSSV: 25110371) — *Phần III: Decision Framework, Kiến trúc Hệ thống & Q&A*

---

## 📂 Cấu Trúc Thư Mục Repository

```text
├── index.html                           # File trình chiếu Reveal.js chính (25 Slides)
├── slides/                              # 25 file component HTML của từng slide
│   ├── slide_00.html                    # Trang bìa & Giới thiệu
│   ├── slide_01.html                    # Mục lục chuyên đề
│   ├── ...                              # Các slide nội dung chi tiết
│   └── slide_23.html                    # Biến thể nâng cao & Lời cảm ơn
├── data/                                # Báo cáo chuyên đề & Tài liệu tham khảo (PDF, DOCX)
├── kich_ban_thuyet_trinh_dsa_chuong_15.md # Kịch bản thuyết trình chi tiết 25 slide & Cẩm nang Q&A
├── build_slides.py                      # Script tự động ghép các slide HTML vào index.html
├── add_agenda_slide.py                  # Script tiện ích tạo slide mục lục
└── README.md                            # Tài liệu hướng dẫn sử dụng repo
```

---

## 🚀 Hướng Dẫn Chạy & Trình Chiếu

### 1. Xem Slide Trình Chiếu
- Mở trực tiếp file `index.html` bằng bất kỳ trình duyệt web hiện đại nào (Google Chrome, Microsoft Edge, Firefox, Brave,...).
- Hoặc sử dụng extension **Live Server** trên VS Code để khởi chạy máy chủ cục bộ.
- **Phím tắt điều khiển (Reveal.js):**
  - Phím `F`: Chuyển sang chế độ toàn màn hình (Fullscreen).
  - Phím `Mũi tên phải (->)` hoặc `Space`: Chuyển sang slide tiếp theo.
  - Phím `Mũi tên trái (<-)`: Quay lại slide trước.
  - Phím `ESC` hoặc `O`: Xem tổng quan bản đồ tất cả các slide (Overview mode).

### 2. Tự Động Build Lại Slide
Nếu bạn chỉnh sửa mã nguồn của các slide lẻ trong thư mục `slides/`, chỉ cần chạy lệnh sau để cập nhật lại `index.html`:

```bash
python build_slides.py
```

---

## 📑 Kịch Bản Thuyết Trình
Toàn bộ lời thoại, phân tích kỹ thuật chuyên sâu (Memory Locality, Pointer Chasing, hàm ngược Ackermann $\alpha(N)$, Path Compression) và bộ câu hỏi phản biện dự phòng (Q&A) đã được chuẩn bị đầy đủ tại:  
👉 **[kich_ban_thuyet_trinh_dsa_chuong_15.md](./kich_ban_thuyet_trinh_dsa_chuong_15.md)**
