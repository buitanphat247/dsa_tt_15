# 🎙️ KỊCH BẢN THUYẾT TRÌNH TOÀN DIỆN 25 SLIDE & CẨM NANG BỔ NGHĨA KỸ THUẬT
## CHƯƠNG 15: CẤU TRÚC DỮ LIỆU CHUYÊN BIỆT (TRIE & UNION-FIND)
### *Tối Ưu Hóa Truy Vấn Chuỗi Tiền Tố & Quản Lý Tập Hợp Rời Rạc Trong Hệ Thống Hiệu Năng Cao*

---

- **Môn học:** Cấu trúc Dữ liệu & Giải thuật (Data Structures & Algorithms)
- **Lớp / Nhóm:** DASA230179_06
- **Giảng viên hướng dẫn:** Thầy Vũ Đình Bảo (T-Bao)
- **Danh sách diễn giả (3 Thành viên):**
  1. **Lê Thị Tuyết Nhi** (MSSV: 25110283) — *Phần I: Đặt vấn đề, Giới hạn CSDL & Cấu trúc Trie (Slide 00 – Slide 11)*
  2. **Mai Thanh Trà** (MSSV: 25110372) — *Phần II: Cấu trúc Union-Find (DSU) & Thuật toán Kruskal (Slide 12 – Slide 20)*
  3. **Huỳnh Thị Thùy Trang** (MSSV: 25110371) — *Phần III: Khung quyết định, Kiến trúc Hệ thống, Mở rộng Nâng cao & Q&A (Slide 21 – Slide 23)*

---

## ⏱️ PHÂN BỔ THỜI LƯỢNG & MA TRẬN PHÂN CÔNG BÁO CÁO

| Diễn giả | Slide | Nội dung trọng tâm | Mục tiêu nhận thức của người nghe | Thời lượng |
| :--- | :--- | :--- | :--- | :--- |
| **Lê Thị Tuyết Nhi** | Slide 00 – 11 *(12 slide)* | Đặt vấn đề, Giới hạn CSDL tổng quát, Memory Locality, Cấu trúc Trie & Phân tích Child Containers | Hiểu vì sao Hash Table thất bại ở Prefix Search, nắm vững cấu trúc hình học Trie, cơ chế cờ `is_end_of_word` và đánh đổi bộ nhớ CPU Cache. | **~7.5 phút** |
| **Mai Thanh Trà** | Slide 12 – 20 *(9 slide)* | Dynamic Connectivity, ADT Disjoint-Set, Nguy cơ suy biến cây, Union by Rank, Path Compression, Ackermann $\alpha(N)$, Trace Table & Kruskal MST | Hiểu cơ chế Up-Tree trên mảng 1D, vì sao kết hợp Rank + Path Compression đạt tốc độ tiệm cận $O(1)$, và ứng dụng Kruskal tìm cây khung. | **~6.5 phút** |
| **Huỳnh Thị Thùy Trang** | Slide 21 – 23 *(4 slide)* | Technical Decision Framework, Bài học Kiến trúc Hệ thống, Biến thể nâng cao (Radix Tree, TST, Rollback DSU) & Điều phối Q&A | Nắm trọn khung tư duy chọn CSDL theo Query Pattern, nguyên lý Trade-off và sẵn sàng phản biện học thuật với Giảng viên. | **~4.0 phút** |
| **Cả nhóm** | Q&A | Trả lời chất vấn của Giảng viên & Sinh viên | Thể hiện tư duy phản biện, chiều sâu cài đặt mã nguồn C++ và tối ưu phần cứng. | **~5.0 phút** |

---

# 📘 PHẦN 1: ĐẶT VẤN ĐỀ, GIỚI HẠN CSDL & CẤU TRÚC TRIE
> **Diễn giả:** Lê Thị Tuyết Nhi (MSSV: 25110283)  
> **Thời lượng dự kiến:** 7 phút 30 giây (Slide 00 – Slide 11)

---

### 📍 SLIDE 00: TRANG BÌA CHUYÊN ĐỀ & GIỚI THIỆU NHÓM
* **Thời lượng:** 40 giây.
* **Hành động trình chiếu:** Bật Slide 00. Đứng thẳng, tự tin, mắt nhìn bao quát Thầy và cả lớp, nụ cười chào đón.

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **Mục tiêu của slide:** Tạo ấn tượng chuyên nghiệp đầu tiên. Cần giới thiệu rõ chuyên đề không chỉ là học lý thuyết cấu trúc dữ liệu, mà đặt trọng tâm vào *"Hệ thống hiệu năng cao (High-Performance Systems)"* — tức là các bài toán hàng triệu người dùng, yêu cầu phản hồi dưới vài miligiây.
> * **Từ khóa then chốt:** *Specialized Data Structures (Cấu trúc Dữ liệu Chuyên biệt)*, *Prefix Tree (Cây tiền tố)*, *Disjoint-Set Union (Tập hợp rời rạc)*.

**🎙️ Lời thoại thuyết minh (Nhi):**
> *"Kính chào Thầy Vũ Đình Bảo cùng toàn thể các bạn sinh viên đang có mặt trong buổi báo cáo chuyên đề hôm nay.*
>
> *Em tên là Lê Thị Tuyết Nhi, đại diện cho Nhóm DASA230179_06. Nhóm chúng em gồm 3 thành viên: Em, bạn Mai Thanh Trà và bạn Huỳnh Thị Thùy Trang. Hôm nay, nhóm xin phép được trình bày chuyên đề nghiên cứu **Chương 15: Cấu Trúc Dữ Liệu Chuyên Biệt (Specialized Data Structures)** với chủ đề trọng tâm: **Trie và Union-Find trong Hệ Thống Hiệu Năng Cao**.*
>
> *Hy vọng bài báo cáo sẽ mang đến cho Thầy và các bạn một góc nhìn sâu sắc từ lý thuyết giải thuật cho đến bản chất tối ưu phần cứng trong thực tế kỹ thuật phần mềm. Sau đây, em xin phép bắt đầu!"*

---

### 📍 SLIDE 01: MỤC LỤC CHUYÊN ĐỀ CHI TIẾT
* **Thời lượng:** 35 giây.
* **Hành động trình chiếu:** Chuyển Slide 01. Dùng tay hoặc bút laser quét qua 4 hộp thẻ Mục lục.

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **Mục tiêu:** Cung cấp "bản đồ tư duy" cho người nghe. Khán giả cần biết bài báo cáo đi theo cấu trúc: Đặt vấn đề -> Giải pháp 1 (Trie) -> Giải pháp 2 (DSU) -> Tổng hợp & Khung quyết định.

**🎙️ Lời thoại thuyết minh (Nhi):**
> *"Bài báo cáo của nhóm chúng em được cấu trúc chặt chẽ qua 4 phần cốt lõi:*
> * **Phần I:** Khảo sát giới hạn của các cấu trúc dữ liệu tổng quát quen thuộc và lý giải nguyên nhân dẫn đến nghẽn hiệu năng khi dữ liệu mở rộng quy mô lớn.
> * **Phần II:** Đi sâu vào Cấu trúc **Trie (Prefix Tree)** — giải pháp chuyên biệt cho bài toán chuỗi và tiền tố.
> * **Phần III:** Khám phá Cấu trúc **Union-Find (DSU)** — thuật toán quản lý tập hợp rời rạc với tốc độ tiệm cận thời gian thực.
> * **Phần IV:** Đánh giá thực nghiệm, Khung quyết định kiến trúc và Hướng phát triển nâng cao.*
>
> *Bây giờ, chúng ta hãy cùng bước vào Phần đầu tiên: Giới hạn của các cấu trúc dữ liệu tổng quát."*

---

### 📍 SLIDE 02: GIỚI HẠN CỦA CẤU TRÚC DỮ LIỆU TỔNG QUÁT
* **Thời lượng:** 50 giây.
* **Hành động trình chiếu:** Chuyển Slide 02. Nhấn mạnh sự đối lập giữa "Hộp công cụ tiêu chuẩn" và "Điểm nghẽn khi Scaling".

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **Bản chất vấn đề:** Các cấu trúc học ở các chương trước (Mảng, Linked List, BST, Hash Table) gọi là *General-Purpose* (đa năng, tổng quát). Chúng rất tốt cho các bài toán cơ bản nhưng có những điểm yếu chết người:
>   1. **Array / Linked List:** Tìm kiếm tiền tố phải quét toàn bộ danh sách $O(N \cdot L)$, với $N$ là số từ, $L$ là độ dài từ.
>   2. **Balanced BST (AVL / Red-Black Tree):** Tra cứu tốn $O(L \cdot \log N)$, phải so sánh chuỗi từng ký tự ở mỗi nút.
>   3. **Hash Table:** Rất mạnh ở tra cứu chính xác ($O(L)$), **nhưng hàm Hash phá hủy hoàn toàn thứ tự từ điển và không thể tìm kiếm tiền tố**. Muốn tìm tiền tố với Hash Table, ta buộc phải duyệt qua toàn bộ $N$ phần tử ($O(N)$)!
> * **Thông điệp:** "Không có cấu trúc vạn năng — Đa năng đồng nghĩa với việc không tối ưu cho bài toán đặc thù."

**🎙️ Lời thoại thuyết minh (Nhi):**
> *"Trong lập trình hàng ngày, chúng ta đều rất quen thuộc với 'Bộ tứ công cụ tiêu chuẩn': Mảng, Danh sách liên kết, Cây nhị phân tìm kiếm (BST) và Bảng băm (Hash Table).*
>
> *Tuy nhiên, khi đưa vào các hệ thống dữ liệu lớn với hàng triệu phần tử, các cấu trúc tổng quát này lập tức bộc lộ điểm nghẽn nghiêm trọng:*
> * Nếu dùng **Mảng hoặc Danh sách liên kết**, phép tìm kiếm tiền tố buộc phải duyệt tuần tự tốn $O(N \cdot L)$ — quá chậm!
> * Nếu dùng **Cây BST cân bằng**, thời gian tìm kiếm bị đội lên $O(L \cdot \log N)$ do phải so sánh chuỗi qua nhiều tầng cây.
> * Còn với **Bảng băm (Hash Table)** — dù tra cứu chính xác đạt tốc độ $O(L)$, nhưng bản chất hàm băm là xáo trộn ngẫu nhiên dữ liệu, **phá hủy hoàn toàn tính liên tục của tiền tố**. Để tìm tất cả các từ bắt đầu bằng một tiền tố, Hash Table không có cách nào khác ngoài việc duyệt cạn toàn bộ $N$ phần tử!*
>
> *Chính vì vậy, chúng ta cần những cấu trúc dữ liệu chuyên biệt hơn!"*

---

### 📍 SLIDE 02_B: VÍ DỤ MINH HỌA 2 BÀI TOÁN THỰC TẾ THÁCH THỨC
* **Thời lượng:** 50 giây.
* **Hành động trình chiếu:** Chuyển Slide 02_b. Chỉ vào 2 tình huống thực tế: Autocomplete và Quan hệ Bạn bè.

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **Bài toán 1 (Autocomplete):** Khi gõ `"app"` trên điện thoại, hệ thống phải trả về ngay `"apple"`, `"application"`, `"apply"` trong vòng dưới 10ms giữa từ điển 1,000,000 từ. Nếu duyệt tuyến tính, người dùng sẽ thấy giật lag rõ rệt.
> * **Bài toán 2 (Dynamic Connectivity):** Trong mạng xã hội 100 triệu tài khoản, người dùng liên tục kết bạn (`union`). Hệ thống cần trả lời ngay lập tức: *"Người A và Người B có nằm trong cùng một nhóm bạn chung hay không?"* (`connected`). Dùng BFS/DFS mỗi lần kiểm tra sẽ tốn $O(V + E)$ — hệ thống sẽ tê liệt ngay lập tức.

**🎙️ Lời thoại thuyết minh (Nhi):**
> *"Để thấy rõ sự cấp thiết, hãy xem xét 2 bài toán thực tế cực kỳ phổ biến sau đây:*
>
> * **Bài toán thứ nhất: Gợi ý từ khi gõ phím (Autocomplete)**. Khi các bạn gõ cụm từ `'app'`, bàn phím điện thoại hay thanh tìm kiếm phải gợi ý ngay lập tức các từ như *'apple'*, *'apply'*, *'application'* từ một bộ từ điển hơn 1 triệu từ trong thời gian dưới 10 mili-giây. Dùng các cấu trúc thông thường chắc chắn sẽ gây hiện tượng đứng máy hoặc trễ giao diện!
> * **Bài toán thứ hai: Kiểm tra quan hệ liên thông bạn bè Real-time**. Trong một mạng xã hội có 100 triệu người dùng, các hành động kết bạn diễn ra liên tục từng giây. Làm thế nào để kiểm tra ngay lập tức xem hai người dùng bất kỳ có liên thông với nhau hay không mà không cần phải duyệt lại toàn bộ đồ thị bằng BFS hay DFS tốn hàng giây?*
>
> *Hai bài toán kinh điển này chính là đất diễn hoàn hảo cho **Trie** và **Union-Find**."*

---

### 📍 SLIDE 03: TRIẾT LÝ "QUERY PATTERN FIRST — STRUCTURE SECOND"
* **Thời lượng:** 45 giây.
* **Hành động trình chiếu:** Chuyển Slide 03. Nhấn mạnh câu khẩu hiệu trên đỉnh slide và 2 nhánh phân loại bên dưới.

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **Triết lý kiến trúc:** Không bao giờ chọn CSDL theo cảm tính ("quen dùng cái gì thì chọn cái đó"). Kỹ sư phần mềm giỏi luôn nhìn vào **Mẫu truy vấn (Query Pattern)** trước:
>   * Nếu mẫu truy vấn là **Prefix Matching / String Indexing** (tìm theo đầu mút chuỗi) $\to$ Chọn **Trie**.
>   * Nếu mẫu truy vấn là **Equivalence Relation / Dynamic Connectivity** (gộp nhóm, kiểm tra cùng nhóm) $\to$ Chọn **Union-Find**.

**🎙️ Lời thoại thuyết minh (Nhi):**
> *"Từ những phân tích trên, nhóm chúng em muốn nhấn mạnh một triết lý thiết kế cốt lõi trong ngành kỹ thuật phần mềm: **'Query Pattern First — Structure Second' (Xác định Mẫu Truy Vấn Trước — Chọn Cấu Trúc Dữ Liệu Sau)**.*
>
> *Thay vì chọn cấu trúc dữ liệu theo thói quen, chúng ta phải phân tích bản chất của luồng truy vấn:*
> * Nếu hệ thống yêu cầu tìm kiếm tiền tố chuỗi, gợi ý từ khóa, hoặc tìm tiền tố chung dài nhất $\to$ Hãy nghĩ ngay đến **Cây Tiền Tố Trie** với thời gian tra cứu chỉ phụ thuộc vào độ dài từ $L$, hoàn toàn độc lập với tổng số từ $N$.*
> * Nếu hệ thống yêu cầu quản lý các nhóm đối tượng động, kiểm tra liên thông hoặc phát hiện chu trình trên đồ thị $\to$ Hãy chọn **Union-Find (DSU)** với tốc độ gần như hằng số $O(1)$.*
>
> *Và để hiểu tại sao các cấu trúc này lại nhanh đến vậy, chúng ta cần nhìn sâu xuống tầng kiến trúc phần cứng máy tính."*

---

### 📍 SLIDE 04: MEMORY LOCALITY & TÁC ĐỘNG PHẦN CỨNG CPU CACHE
* **Thời lượng:** 50 giây.
* **Hành động trình chiếu:** Chuyển Slide 04. Chỉ vào 2 cột so sánh: "Pointer Chasing" bên trái và "Spatial Locality / Cache Line" bên phải.

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **Vấn đề phần cứng:** CPU ngày nay chạy cực nhanh (vài GHz), nhưng tốc độ RAM lại chậm hơn CPU hàng trăm lần ( hiện tượng *Memory Wall*).
> * **Pointer Chasing (Đuổi bắt con trỏ):** Khi dùng Linked List hay Tree cấp phát rời rạc bằng `new`, các nút nằm rải rác khắp nơi trên Heap. Mỗi lần nhảy sang con trỏ tiếp theo, CPU bị **Cache Miss** và phải mất ~100 đến 200 chu kỳ chờ nạp dữ liệu từ RAM chính vào L1/L2 Cache.
> * **Spatial Locality (Tính cục bộ không gian):** Khi dữ liệu nằm trên mảng liên tục, mỗi lần CPU đọc 1 phần tử, nó sẽ tiện tay nạp luôn cả một khối **64-byte Cache Line** chứa các phần tử liền kề vào L1 Cache (chỉ mất ~4 chu kỳ).
> * **Ý nghĩa với Trie:** Nắm được điều này giúp ta hiểu vì sao việc thiết kế mảng con (`children[26]`) hay cấu trúc nút trong Trie lại ảnh hưởng trực tiếp đến hiệu năng thực tế của CPU.

**🎙️ Lời thoại thuyết minh (Nhi):**
> *"Một thuật toán có độ phức tạp lý thuyết Big-O tốt chưa chắc đã chạy nhanh trong thực tế nếu nó đi ngược lại cơ chế hoạt động của phần cứng CPU.*
>
> *Trên màn hình là sự đối lập về mặt **Bộ nhớ cục bộ (Memory Locality)**:*
> * Ở các cấu trúc dùng nhiều con trỏ phân tán như Danh sách liên kết hay Cây nhị phân, hiện tượng **'Pointer Chasing'** xảy ra. Do các nút nằm rải rác trên Heap, CPU liên tục gặp **Cache Miss** và phải chờ từ 100 đến 200 chu kỳ xung nhịp để kéo dữ liệu từ RAM chính về!*
> * Ngược lại, các cấu trúc tối ưu sẽ tận dụng **Spatial Locality (Tính cục bộ không gian)**. Khi đọc một phần tử trên mảng liên tục, CPU sẽ tự động nạp luôn một khối **Cache Line 64-byte** chứa các dữ liệu lân cận vào L1 Cache với độ trễ chỉ vỏn vẹn 4 chu kỳ xung nhịp!*
>
> *Hiểu rõ điều này sẽ giúp chúng ta đưa ra những quyết định cài đặt cấu trúc Trie tối ưu nhất cho bộ nhớ đệm."*

---

### 📍 SLIDE 05: BÀI TOÁN AUTOCOMPLETE & SO SÁNH HIỆU NĂNG BIG-O
* **Thời lượng:** 45 giây.
* **Hành động trình chiếu:** Chuyển Slide 05. Dẫn dắt ánh nhìn khán giả qua từng hàng của Bảng so sánh Big-O.

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **Ký hiệu:** $N$ = tổng số từ trong từ điển, $L$ = độ dài tối đa của một từ, $P$ = độ dài tiền tố đang tìm, $K$ = số lượng từ khớp với tiền tố trả về.
> * **Nhận xét cốt lõi:**
>   * Mảng (Array): Chèn $O(1)$ hoặc $O(N \cdot L)$ nếu có sort, nhưng Prefix Search cực chậm $O(N \cdot L)$.
>   * Hash Table: Tra cứu chính xác $O(L)$ vô địch, nhưng Prefix Search bắt buộc phải quét hết $O(N \cdot L)$.
>   * **Trie:** Prefix Search chỉ tốn $O(P + K)$! Chỉ đi đúng $P$ bước theo độ dài tiền tố, sau đó duyệt cây con lấy $K$ từ. **Hoàn toàn độc lập với $N$ (dù từ điển có 10 triệu từ thì thời gian vẫn như 1,000 từ)!**

**🎙️ Lời thoại thuyết minh (Nhi):**
> *"Bây giờ, chúng ta hãy đặt 3 cấu trúc lên bàn cân trong bài toán Autocomplete qua bảng phân tích Big-O:*
>
> * Với **Mảng thông thường**: Tìm kiếm tiền tố mất $O(N \cdot L)$ — quy mô dữ liệu $N$ càng lớn thì hệ thống càng chậm.
> * Với **Bảng băm (Hash Table)**: Mặc dù tra cứu từ chính xác rất nhanh $O(L)$, nhưng tìm kiếm tiền tố vẫn bị vướng mức $O(N \cdot L)$ vì không thể tận dụng cấu trúc băm cho tiền tố.
> * Và ngôi sao của chúng ta — **Cây Trie**: Thời gian tìm kiếm tiền tố chỉ là **$O(P + K)$**, trong đó $P$ là độ dài tiền tố và $K$ là số lượng kết quả gợi ý.
>
> *Điều kỳ diệu ở đây là: **Thời gian truy vấn hoàn toàn không phụ thuộc vào tổng số từ $N$ trong cơ sở dữ liệu**! Dù từ điển có 1 vạn hay 100 triệu từ, tốc độ tìm kiếm tiền tố vẫn nhanh như nhau!"*

---

### 📍 SLIDE 06: CẤU TRÚC HÌNH HỌC ĐẶC BIỆT CỦA CÂY TRIE
* **Thời lượng:** 50 giây.
* **Hành động trình chiếu:** Chuyển Slide 06. Chỉ vào sơ đồ cây Trie với các vòng tròn Node và mũi tên Edge ký tự.

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **3 nguyên lý hình học sống còn của Trie:**
>   1. **Nút (Node) = Điểm giao rỗng:** Nút không chứa ký tự! Nút chỉ đóng vai trò là một "ngã rẽ" (State / Junction).
>   2. **Cạnh (Edge) = Ký tự chuyển tiếp (Transition):** Ký tự thực sự nằm trên đường liên kết giữa nút cha và nút con.
>   3. **Từ khóa (Word) = Đường đi (Path):** Một từ hoàn chỉnh được hình thành bằng cách đi từ Gốc (Root) men theo các cạnh xuống dưới.
>   * **Nút Gốc (Root):** Luôn là nút rỗng, đại diện cho chuỗi rỗng `""`.

**🎙️ Lời thoại thuyết minh (Nhi):**
> *"Vậy cấu trúc bên trong của một cây Trie được tổ chức như thế nào? Cây Trie sở hữu 3 nguyên lý hình học rất đặc biệt:*
>
> * **Thứ nhất, Nút (Node) là một Điểm giao rỗng**: Khác với cây nhị phân lưu trữ giá trị tại nút, nút trong Trie không trực tiếp chứa ký tự. Nó đóng vai trò như một ngã rẽ trạng thái. Đặc biệt, Nút Gốc (Root) luôn là nút rỗng đại diện cho chuỗi ban đầu.
> * **Thứ hai, Cạnh (Edge) chính là Ký tự**: Ký tự thực chất được biểu diễn bởi chỉ số của cạnh liên kết từ nút cha trỏ tới nút con.
> * **Thứ ba, Từ khóa là một Đường đi (Path)**: Một từ hoàn chỉnh được tạo thành bằng cách đi từ nút Gốc lần lượt qua các cạnh ký tự cho tới nút đích.
>
> *Nhờ mô hình này, tất cả các từ có chung phần đầu sẽ đi chung trên cùng một lộ trình, giúp triệt tiêu hoàn toàn sự dư thừa dữ liệu!"*

---

### 📍 SLIDE 07: VAI TRÒ CỦA CỜ `is_end_of_word` TRONG CÂY TRIE
* **Thời lượng:** 50 giây.
* **Hành động trình chiếu:** Chuyển Slide 07. Chỉ vào nút có viền đôi / màu sắc đánh dấu `is_end_of_word = true` (ví dụ từ `"cat"` nằm trong `"caterpillar"`).

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **Tại sao cần cờ này?** Cây Trie lưu trữ rất nhiều chuỗi lồng nhau.
>   * Ví dụ: Ta chèn từ `"caterpillar"`. Nếu người dùng tìm từ `"cat"`, ta thấy trên đường đi có các cạnh `'c' \to 'a' \to 't'`. Nhưng làm sao máy tính biết `"cat"` có phải là một từ có nghĩa trong từ điển hay chỉ là một đoạn tiền tố vô tình đi qua?
>   * **Cờ `is_end_of_word = true`** tại nút `'t'` sẽ khẳng định: *"Tại đây kết thúc một từ hợp lệ mang tên `'cat'`"*.
> * **Phân biệt sống còn:** Nút lá hình học (Leaf - nút không có con) khác hoàn toàn với Nút kết thúc từ (End of word - nút có cờ bật, vẫn có thể có con như `'cat'` là tiền tố của `'caterpillar'`).

**🎙️ Lời thoại thuyết minh (Nhi):**
> *"Một thành phần không thể thiếu trong mỗi `TrieNode` chính là biến cờ hiệu boolean mang tên `is_end_of_word`.*
>
> *Tại sao cờ hiệu này lại mang tính sống còn?*
> * Hãy lấy ví dụ: Chúng ta lưu từ `'caterpillar'` vào Trie. Rõ ràng trên đường đi có chứa nhánh `'c' \to 'a' \to 't'`.
> * Nếu không có cờ `is_end_of_word`, khi người dùng tìm kiếm từ `'cat'`, hệ thống sẽ bị bối rối: Liệu `'cat'` là một từ có nghĩa độc lập trong từ điển, hay nó chỉ là một đoạn tiền tố vô nghĩa nằm bên trong từ `'caterpillar'`?
> * Khi ta bật cờ `is_end_of_word = true` tại nút `'t'`, cây Trie sẽ xác nhận: `'cat'` là một từ hoàn chỉnh, đồng thời vẫn cho phép các nhánh con tiếp tục kéo dài tới `'caterpillar'`.
>
> *Nhờ cờ hiệu này, chúng ta phân biệt rạch ròi giữa khái niệm 'Nút lá hình học' và 'Từ hợp lệ', cho phép nén hàng vạn từ lồng nhau một cách an toàn tuyệt đối!"*

---

### 📍 SLIDE 08: THUẬT TOÁN VẬN HÀNH TRIE & MÔ PHỎNG TUẦN TỰ
* **Thời lượng:** 60 giây.
* **Hành động trình chiếu:** Chuyển Slide 08. Chỉ vào các khối mã nguồn C++ của `insert`, `search`, `startsWith` và `delete`.

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **4 phương thức cốt lõi:**
>   1. `insert(word)`: Lặp qua từng ký tự `c`, tính `index = c - 'a'`. Nếu `children[index] == nullptr` thì cấp phát nút mới. Tới ký tự cuối thì gán `is_end = true`. Độ phức tạp $O(L)$.
>   2. `search(word)`: Đi theo từng ký tự, nếu gặp `nullptr` $\to$ `false`. Đi hết chuỗi mà `is_end == true` $\to$ `true`.
>   3. `startsWith(prefix)`: Tương tự `search`, nhưng chỉ cần đi hết chuỗi prefix mà không bị `nullptr` là trả về `true` ngay (không cần kiểm tra `is_end`).
>   4. `delete(word)`: Sử dụng **đệ quy từ dưới lên (Post-order Traversal)**. Nếu nút đó không còn là tiền tố của từ nào khác và không có con (`has_no_children`), ta giải phóng bộ nhớ (`delete`) ngược dần lên để tránh rò rỉ RAM (Memory Leak).

**🎙️ Lời thoại thuyết minh (Nhi):**
> *"Trên màn hình là cài đặt C++ chuẩn mực cho 4 thao tác vận hành trên cây Trie:*
>
> 1. **Phép Chèn (`insert`)**: Ta duyệt qua từng ký tự của từ, tính chỉ số `index = c - 'a'`. Nếu con trỏ `children[index]` đang rỗng (`nullptr`), ta cấp phát một `TrieNode` mới và di chuyển xuống. Tại ký tự cuối cùng, ta bật cờ `is_end = true`. Toàn bộ quá trình chỉ mất đúng **$O(L)$**.
> 2. **Phép Tìm kiếm chính xác (`search`)**: Duyệt theo chuỗi ký tự. Nếu đi hết từ mà gặp nút có cờ `is_end == true`, ta trả về `true`. Ngược lại nếu đứt đoạn giữa chừng, trả về `false`.
> 3. **Phép Kiểm tra tiền tố (`startsWith`)**: Cực kỳ tinh gọn! Ta chỉ cần duyệt hết độ dài tiền tố, nếu mọi nhánh đều tồn tại thì lập tức trả về `true` mà không cần kiểm tra cờ kết thúc từ.
> 4. **Phép Xóa từ (`delete`)**: Được xử lý bằng tư duy đệ quy từ dưới lên. Nếu sau khi tắt cờ `is_end`, nút đó không còn nút con nào khác, thuật toán sẽ chủ động giải phóng bộ nhớ ngược lên trên để bảo đảm không bị rò rỉ tài nguyên RAM."*

---

### 📍 SLIDE 09: HIỆN TƯỢNG DÙNG CHUNG TIỀN TỐ (PREFIX SHARING)
* **Thời lượng:** 45 giây.
* **Hành động trình chiếu:** Chuyển Slide 09. Chỉ vào ví dụ nén 7 từ tiếng Anh thành 16 nút Trie.

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **Số liệu thực tế:** 7 từ: `app`, `apple`, `apply`, `apt`, `bat`, `bath`, `batch`.
>   * Nếu lưu mảng/string rời: $3 + 5 + 5 + 3 + 3 + 4 + 5 = 28$ ký tự.
>   * Khi nén trong Trie: Chỉ tốn **16 nút**.
>   * **Tỷ lệ tiết kiệm:** Giảm gần **46.7%** số nút cần lưu trữ nhờ hiện tượng dùng chung tiền tố (Prefix Sharing).
> * **Tính chất tự nhiên:** Các từ tự động được sắp xếp theo thứ tự bảng chữ cái (Lexicographical Order) khi duyệt cây theo thứ tự tiền thứ tự (Pre-order Traversal).

**🎙️ Lời thoại thuyết minh (Nhi):**
> *"Sức mạnh tiết kiệm không gian của Trie đến từ cơ chế **Dùng Chung Tiền Tố (Prefix Sharing)**.*
>
> *Hãy quan sát ví dụ trên Slide với 7 từ: `'app'`, `'apple'`, `'apply'`, `'apt'`, `'bat'`, `'bath'`, `'batch'`.*
> * Nếu lưu trữ độc lập theo dạng mảng chuỗi truyền thống, chúng ta tiêu tốn tổng cộng 28 ký tự.
> * Nhưng khi đưa vào cây Trie, toàn bộ 7 từ này được nén gọn lại chỉ trong **16 nút duy nhất**, giảm tới **46.7%** dung lượng lưu trữ!
>
> *Các từ như `'apple'` và `'apply'` cùng chia sẻ toàn bộ nhánh `'a' \to 'p' \to 'p'`. Đồng thời, một ưu điểm tự nhiên rất đẹp là khi ta duyệt cây Trie theo thứ tự Pre-order, toàn bộ các từ sẽ tự động xuất hiện theo đúng **thứ tự từ điển (Lexicographical Order)** mà không tốn thêm bất kỳ chi phí sắp xếp nào!"*

---

### 📍 SLIDE 10: PHÂN TÍCH ĐÁNH ĐỔI CHILD CONTAINER
* **Thời lượng:** 50 giây.
* **Hành động trình chiếu:** Chuyển Slide 10. So sánh 3 cột: Fixed Array, Hash Map và Sorted Vector.

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **Đây là câu hỏi phỏng vấn Big Tech & câu hỏi Thầy rất thích hỏi:** Trong `TrieNode`, nên dùng container nào để chứa con trỏ con?
>   1. **Mảng tĩnh `Fixed Array [26]`:**
>      * *Ưu điểm:* Truy cập cực nhanh $O(1)$, cache locality hoàn hảo.
>      * *Nhược điểm:* Rất tốn RAM nếu dữ liệu thưa thớt (26 con trỏ $\times$ 8 bytes = 208 bytes/nút dù chỉ dùng 1-2 ký tự). Không mở rộng được cho bảng chữ cái Unicode (hàng ngàn ký tự).
>   2. **Bảng băm `std::unordered_map`:**
>      * *Ưu điểm:* Tiết kiệm RAM khi phân nhánh thưa, hỗ trợ toàn bộ bảng chữ cái Unicode/UTF-8.
>      * *Nhược điểm:* Overhead tính hàm băm, va chạm (collisions), pointer chasing gây cache miss.
>   3. **Mảng động đã sắp xếp `std::vector`:**
>      * *Ưu điểm:* Tiết kiệm RAM, bộ nhớ liên tục.
>      * *Nhược điểm:* Tìm kiếm con tốn $O(\log R)$ bằng Binary Search.

**🎙️ Lời thoại thuyết minh (Nhi):**
> *"Một câu hỏi kỹ thuật rất sâu sắc khi lập trình Trie: **Chúng ta nên chọn cấu trúc nào để quản lý các nút con (`child container`)?** Không có câu trả lời duy nhất, mà là sự đánh đổi kỹ thuật:*
>
> * **Lựa chọn 1: Mảng cố định `Fixed Array [26]`**: Mang lại tốc độ truy xuất $O(1)$ tuyệt đối và thân thiện nhất với bộ nhớ đệm CPU Cache. Tuy nhiên nhược điểm là rất tốn bộ nhớ nếu cây phân nhánh thưa thớt và chỉ giới hạn trong bảng chữ cái tiếng Anh 26 ký tự.
> * **Lựa chọn 2: Bảng băm `std::unordered_map`**: Tiết kiệm bộ nhớ tuyệt vời cho cây thưa và hỗ trợ toàn bộ tập ký tự Unicode quốc tế, nhưng bù lại phải đánh đổi chi phí tính toán hàm băm và tăng độ trễ Cache Miss.
> * **Lựa chọn 3: Mảng co giãn `Sorted std::vector`**: Giải pháp cân bằng hoàn hảo cho các tập ký tự động kích thước vừa phải.
>
> *Tùy vào tài nguyên hệ thống và bảng chữ cái mục tiêu mà người kỹ sư sẽ lựa chọn container phù hợp."*

---

### 📍 SLIDE 11: BEST PRACTICES & 4 ỨNG DỤNG THỰC TẾ CỦA TRIE
* **Thời lượng:** 45 giây.
* **Hành động trình chiếu:** Chuyển Slide 11. Chỉ vào 4 biểu tượng ứng dụng lớn: Gboard, IDE, Router IP, Search Engine. Kết thúc phần I và chuyển giao diễn giả.

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **4 Use Case kinh điển:**
>   1. **Gboard / iOS Keyboard:** Gợi ý từ tiếp theo khi gõ phím.
>   2. **IDE Autocomplete (VS Code, IntelliJ):** Gợi ý tên hàm, tên biến khi gõ code.
>   3. **Network IP Routing:** Thuật toán *Longest Prefix Match* tìm địa chỉ mạng chuyển tiếp gói tin trong router internet.
>   4. **Search Engine Auto-suggest:** Gợi ý câu truy vấn trên Google / Bing.

**🎙️ Lời thoại thuyết minh (Nhi):**
> *"Nhờ những ưu thế vượt trội về mặt tốc độ, Trie được ứng dụng rộng rãi trong các hệ thống phần mềm cốt lõi hàng ngày:*
> 1. *Bàn phím thông minh **Gboard và iOS** để dự đoán từ gõ phím real-time.*
> 2. *Tính năng IntelliSense trên các **IDE như VSCode hay IntelliJ** giúp lập trình viên tự động hoàn thành mã nguồn trong chớp mắt.*
> 3. *Định tuyến mạng viễn thông với thuật toán **Longest Prefix Match** trên các bộ Router Internet.*
> 4. *Và các công cụ **Gợi ý tìm kiếm (Auto-suggest)** của Google hay Bing.*
>
> *Đó là toàn bộ bức tranh về Cấu trúc dữ liệu Trie trong việc xử lý chuỗi và tiền tố.*
>
> *Tiếp theo đây, để giải quyết bài toán liên thông động và quản lý tập hợp rời rạc với tốc độ tiệm cận thời gian thực, em xin trân trọng kính mời bạn **Mai Thanh Trà** trình bày Cấu trúc dữ liệu vô cùng kỳ diệu: **Union-Find (DSU)**!"*

---

# 📗 PHẦN 2: CẤU TRÚC UNION-FIND (DISJOINT-SET / DSU)
> **Diễn giả:** Mai Thanh Trà (MSSV: 25110372)  
> **Thời lượng dự kiến:** 6 phút 30 giây (Slide 12 – Slide 20)

---

### 📍 SLIDE 12: BÀI TOÁN KẾT NỐI ĐỘNG (DYNAMIC CONNECTIVITY)
* **Thời lượng:** 45 giây.
* **Hành động trình chiếu:** Trà bước lên bục, mỉm cười tự tin, cúi chào Thầy và các bạn. Bật Slide 12.

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **Định nghĩa toán học của Dynamic Connectivity:**
>   * Ta có tập $N$ phần tử $\{0, 1, \dots, N-1\}$.
>   * Quan hệ liên thông là một **Quan hệ tương đương (Equivalence Relation)**, thỏa mãn 3 tính chất:
>     1. *Phản xạ (Reflexive):* $p$ luôn kết nối với $p$.
>     2. *Đối xứng (Symmetric):* Nếu $p$ kết nối $q$ thì $q$ kết nối $p$.
>     3. *Bắc cầu (Transitive):* Nếu $p$ kết nối $q$ và $q$ kết nối $r$ thì $p$ kết nối $r$.
>   * 2 thao tác cơ bản:
>     * `union(p, q)`: Nối 2 phần tử $p$ và $q$ (gộp 2 nhóm lại thành 1).
>     * `connected(p, q)`: Trả về `true` nếu $p$ và $q$ cùng thuộc 1 nhóm, ngược lại `false`.
> * **Tại sao BFS/DFS không tối ưu ở đây?** BFS/DFS chỉ nhanh trên đồ thị tĩnh. Với đồ thị động (liên tục thêm cạnh `union`), mỗi lần gọi `connected` phải duyệt lại toàn bộ đồ thị $O(V + E)$, cực kỳ tốn kém!

**🎙️ Lời thoại thuyết minh (Trà):**
> *"Xin cảm ơn phần trình bày rất trực quan của bạn Tuyết Nhi.*
>
> *Kính chào Thầy Vũ Đình Bảo cùng toàn thể các bạn, em tên là Mai Thanh Trà. Sau đây, em xin phép đại diện nhóm trình bày cấu trúc dữ liệu thứ hai của chuyên đề: **Cấu Trúc Tập Hợp Rời Rạc — Disjoint-Set Union (hay còn gọi là Union-Find / DSU)**.*
>
> *Hãy bắt đầu với **Bài toán Kết nối động (Dynamic Connectivity)**. Chúng ta có $N$ đối tượng ban đầu hoàn toàn tách biệt. Theo thời gian, hệ thống liên tục nhận 2 yêu cầu:*
> 1. *Thao tác `union(u, v)`: Kết nối đối tượng $u$ với $ đối tượng $v$, tức là gộp nhóm chứa $u$ và nhóm chứa $v$ lại làm một.*
> 2. *Thao tác `connected(u, v)`: Kiểm tra xem $u$ và $v$ có đang liên thông với nhau hay không.*
>
> *Đây là một quan hệ tương đương mang đầy đủ tính chất Phản xạ, Đối xứng và Bắc cầu. Nếu giải bài toán này bằng các thuật toán duyệt đồ thị truyền thống như BFS hay DFS, mỗi lần truy vấn sẽ tốn chi phí $O(V + E)$. DSU ra đời với một sứ mệnh duy nhất: **Thực hiện hai thao tác trên với tốc độ tiệm cận hằng số $O(1)$!**"*

---

### 📍 SLIDE 13: DISJOINT-SET ADT & KỸ THUẬT BIỂU DIỄN MẢNG `parent[]`
* **Thời lượng:** 45 giây.
* **Hành động trình chiếu:** Chuyển Slide 13. Chỉ vào sơ đồ chuyển đổi từ Rừng cây (Forest) sang Mảng 1 chiều `parent[]`.

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **Cấu trúc dữ liệu Up-Tree:** Mỗi tập hợp rời rạc được mô hình hóa thành một cây ngược, trong đó nút con trỏ lên nút cha (`parent`). Nút gốc (Root) tự trỏ vào chính nó (`parent[root] == root`).
> * **Biểu diễn phẳng bằng Mảng 1D:** Không cần tạo struct phức tạp hay cấp phát con trỏ! Chỉ cần đúng một mảng số nguyên duy nhất `int parent[N]`.
>   * Khởi tạo: Mỗi phần tử là một tập hợp độc lập $\to$ `parent[i] = i`.
>   * Thao tác `find(i)`: Lần theo `parent[i]` ngược lên cho đến khi gặp nút mà `parent[root] == root`. Nút gốc này chính là "Đại diện / Chủ tịch" của tập hợp.

**🎙️ Lời thoại thuyết minh (Trà):**
> *"Để hiện thực hóa DSU, các nhà khoa học máy tính đã phát minh ra một mô hình cực kỳ thông minh: **Rừng cây hướng gốc (Up-Tree Forest)** và nén toàn bộ cấu trúc đó vào đúng **một mảng 1 chiều `parent[]` duy nhất**!*
>
> *Cơ chế hoạt động vô cùng tinh gọn:*
> * Ban đầu, khi có $N$ phần tử độc lập, mỗi phần tử tự là gốc của chính mình: Ta khởi tạo `parent[i] = i` với mọi $i$.
> * Khi nhiều phần tử thuộc cùng một nhóm, chúng sẽ tạo thành một cây. Trong đó, **Nút Gốc (Root)** của cây đóng vai trò là 'Người Đại Diện' duy nhất cho toàn bộ nhóm đó.
> * Để tìm xem phần tử $i$ thuộc nhóm nào, ta chỉ cần gọi hàm `find(i)` để leo ngược theo con trỏ `parent` lên tới đỉnh Gốc.
> * Hai phần tử $u$ và $v$ được coi là liên thông nếu và chỉ nếu `find(u) == find(v)` — tức là chúng có chung một Người Đại Diện!*
>
> *Một cấu trúc toàn vẹn không hề tốn thêm bất kỳ con trỏ phức tạp nào!"*

---

### 📍 SLIDE 14: MÔ HÌNH ĐẠI DIỆN TẬP HỢP & NGUY CƠ SUY BIẾN
* **Thời lượng:** 50 giây.
* **Hành động trình chiếu:** Chuyển Slide 14. Chỉ vào sơ đồ cây bị suy biến thành danh sách liên kết thẳng đứng `4 -> 3 -> 2 -> 1 -> 0`.

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **Naive Union (Gộp ngây thơ):** Nếu viết hàm gộp đơn giản: `void unionNaive(int u, int v) { parent[find(u)] = find(v); }`.
> * **Hậu quả:** Nếu gộp theo chuỗi thứ tự $0-1, 1-2, 2-3, \dots, (N-1)-N$, cây sẽ bị kéo dài thành một chuỗi thẳng tuột (Skewed Tree / Linked List) có chiều cao $H = N - 1$.
> * **Độ phức tạp thoái hóa:** Mỗi lần gọi `find()`, ta phải đi qua $N$ nút $\to$ Thời gian thoái hóa từ $O(1)$ thành **$O(N)$**!
> * **Kết luận:** Cần giải pháp tối ưu để khống chế chiều cao cây.

**🎙️ Lời thoại thuyết minh (Trà):**
> *"Tuy nhiên, nếu chúng ta chỉ cài đặt phép `union` một cách ngây thơ — tức là cứ tùy tiện nối gốc của cây này vào dưới gốc của cây kia — một thảm họa hiệu năng sẽ xảy ra!*
>
> *Hãy nhìn vào sơ đồ bên phải Slide 14:*
> * Trong trường hợp xấu nhất, nếu các thao tác gộp diễn ra theo một chuỗi tuần tự $0-1$, rồi $1-2$, $2-3$, $3-4$, cây DSU sẽ bị **suy biến hoàn toàn thành một Danh sách liên kết thẳng đứng**!
> * Khi đó, chiều cao của cây chạm ngưỡng tối đa $H = N - 1$.
> * Mỗi lần thực hiện `find()`, thuật toán phải duyệt qua toàn bộ $N$ nút, khiến độ phức tạp bị **thoái hóa nghiêm trọng từ mong đợi hằng số về lại $O(N)$**!
>
> *Để giải quyết triệt để nguy cơ suy biến này, chúng ta có 2 kỹ thuật tối ưu hóa kinh điển: **Union by Rank** và **Path Compression**."*

---

### 📍 SLIDE 15: TỐI ƯU HÓA 1: UNION BY RANK / SIZE
* **Thời lượng:** 45 giây.
* **Hành động trình chiếu:** Chuyển Slide 15. Chỉ vào quy tắc so sánh Rank và đoạn mã C++ `unionByRank`.

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **Rank là gì?** `rank[i]` là một ước lượng chặn trên về chiều cao (depth) của cây có gốc tại $i$. Ban đầu mọi nút có `rank[i] = 0`.
> * **Quy tắc gộp (Heuristic):**
>   * Nếu `rank[rootU] < rank[rootV]`: Nối cây nhỏ $U$ vào dưới cây lớn $V$ $\to$ Chiều cao của $V$ không đổi!
>   * Nếu `rank[rootU] > rank[rootV]`: Nối $V$ vào dưới $U$ $\to$ Chiều cao của $U$ không đổi!
>   * Nếu `rank[rootU] == rank[rootV]`: Chọn 1 cây làm cha và **tăng Rank của cây đó lên 1** (`rank[rootU]++`).
> * **Kết quả toán học:** Chiều cao của cây luôn được khống chế không bao giờ vượt quá $\lfloor\log_2 N\rfloor$. Thời gian tìm kiếm giảm từ $O(N)$ xuống chắc chắn **$O(\log N)$**!

**🎙️ Lời thoại thuyết minh (Trà):**
> *"Kỹ thuật tối ưu đầu tiên là **Union by Rank (Gộp theo Cấp bậc)**.*
>
> *Tư tưởng rất trực quan: Mỗi khi cần sáp nhập 2 nhóm, **ta luôn treo cây có chiều cao (Rank) thấp hơn vào dưới gốc của cây có Rank cao hơn**.*
> * Khi nối cây thấp vào cây cao, chiều cao tổng thể của cây lớn hoàn toàn không bị tăng lên!
> * Chiều cao chỉ tăng thêm đúng 1 đơn vị khi và chỉ khi ta gộp hai cây có Rank hoàn toàn bằng nhau.
>
> *Nhờ nguyên lý thông minh này, chiều cao tối đa của cây luôn được chặn trên ở mức $\log_2 N$. Độ phức tạp của mọi thao tác DSU được kéo giảm ngoạn mục từ $O(N)$ xuống chỉ còn **$O(\log N)$**!"*

---

### 📍 SLIDE 16: TỐI ƯU HÓA 2: NÉN ĐƯỜNG ĐI (PATH COMPRESSION)
* **Thời lượng:** 50 giây.
* **Hành động trình chiếu:** Chuyển Slide 16. Nhấn mạnh dòng lệnh C++ đệ quy 1 dòng và sơ đồ biến đổi cây nhiều tầng thành cây phẳng 1 tầng.

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **Dòng mã đệ quy ma thuật:**  
>   `int find(int i) { if (parent[i] == i) return i; return parent[i] = find(parent[i]); }`
> * **Cơ chế hoạt động:** Trong quá trình hàm `find(i)` đi từ nút $i$ lên gốc $R$, khi đệ quy quay lui trở về (Unwinding), nó gán lại con trỏ `parent` của **tất cả các nút đã đi qua trỏ trực tiếp về $R$**!
> * **Kết quả:** Toàn bộ nhánh cây nhiều tầng bị kéo phẳng hoàn toàn thành cây 1 tầng duy nhất. Tất cả các nút con đều nối thẳng vào Gốc.
> * **Hiệu quả:** Lần gọi `find()` đầu tiên trên nhánh có thể tốn vài bước, nhưng từ lần gọi thứ hai trở đi trên bất kỳ nút nào của nhánh đó, thời gian chỉ tốn đúng **$O(1)$**!

**🎙️ Lời thoại thuyết minh (Trà):**
> *"Nếu Union by Rank đã đưa độ phức tạp về $O(\log N)$, thì kỹ thuật thứ hai — **Path Compression (Nén đường đi)** — mới thực sự là một tuyệt tác thuật toán!*
>
> *Hãy nhìn vào dòng code C++ kỳ diệu này:*
> `return parent[i] = find(parent[i]);`
>
> *Cơ chế hoạt động vô cùng tinh xảo: Trong quá trình đệ quy đi tìm Nút Gốc, trên đường quay lui trở về, thuật toán sẽ **bẻ thẳng toàn bộ các nút đã đi qua để nối trực tiếp vào Nút Gốc**!*
> * Cấu trúc cây nhiều tầng ngay lập tức bị ép phẳng tuyệt đối thành cây chỉ có đúng 1 tầng duy nhất.
> * Tất cả các thao tác `find()` kế tiếp trên các nút này sẽ chạm tới Gốc trong đúng 1 bước nhảy — đạt tốc độ **$O(1)$ tức thì**!
>
> *Đây chính là cơ chế tự tối ưu cấu trúc dữ liệu theo thời gian thực (Self-adjusting data structure)!"*

---

### 📍 SLIDE 17: ĐỘ PHỨC TẠP CỰC HẠN & HÀM NGƯỢC ACKERMANN $\alpha(N)$
* **Thời lượng:** 50 giây.
* **Hành động trình chiếu:** Chuyển Slide 17. Chỉ vào Bảng tra cứu giá trị $N = 10^{80} \implies \alpha(N) \le 4$.

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **Định lý Tarjan (1975):** Khi kết hợp đồng thời cả *Union by Rank* và *Path Compression*, chi phí trung bình (amortized cost) cho mỗi thao tác là **$O(\alpha(N))$**, trong đó $\alpha(N)$ là **Hàm ngược Ackermann (Inverse Ackermann function)**.
> * **Ý nghĩa thực tế của $\alpha(N)$:**
>   * Hàm Ackermann $A(m, n)$ là một trong những hàm tăng nhanh nhất toán học. Do đó hàm ngược $\alpha(N)$ là hàm tăng **chậm nhất** từng được biết đến!
>   * Để $\alpha(N) = 5$, số phần tử $N$ phải vượt quá $2^{2^{2^{65536}}}$ — lớn hơn cả tổng số nguyên tử trong toàn bộ vũ trụ quan sát được ($10^{80}$).
>   * Vì vậy, với mọi bài toán trong thế giới thực và trên mọi siêu máy tính, **$\alpha(N) \le 4$**. Trong thực tế kỹ thuật, ta hoàn toàn coi DSU chạy với **thời gian hằng số $O(1)$**!

**🎙️ Lời thoại thuyết minh (Trà):**
> *"Khi kết hợp đồng thời cả hai kỹ thuật: Union by Rank và Path Compression, chúng ta đạt được một giới hạn lý thuyết tối thượng được nhà khoa học máy tính Robert Tarjan chứng minh vào năm 1975: **$O(\alpha(N))$** cho mỗi thao tác.*
>
> *Trong đó, $\alpha(N)$ là **Hàm ngược Ackermann** — hàm số tăng trưởng chậm nhất trong toàn bộ lịch sử toán học và khoa học máy tính!*
> * Để hàm $\alpha(N)$ đạt tới giá trị bằng 5, số lượng phần tử $N$ cần thiết phải vượt qua $10^{80}$ — tức là nhiều hơn tổng số nguyên tử trong toàn bộ vũ trụ của chúng ta!
> * Do đó, đối với bất kỳ bài toán thực tế nào trên Trái Đất, **$\alpha(N)$ không bao giờ vượt quá 4**.
>
> *Nói cách khác, chúng ta có thể tự tin khẳng định: **DSU đạt hiệu năng tiệm cận hằng số $O(1)$ tuyệt đối** trong mọi hệ thống phần mềm!"*

---

### 📍 SLIDE 18: WORKED EXAMPLE: BẢNG TRACE MÔ PHỎNG DSU
* **Thời lượng:** 50 giây.
* **Hành động trình chiếu:** Chuyển Slide 18. Dùng bút laser chỉ vào từng dòng của Bảng Trace Table, đặc biệt là 2 dòng highlight: Bước 4 (Xanh) và Bước 6 (Tím).

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **Giải thích từng bước chạy vết (Trace):**
>   * *Bước 0:* 6 nút độc lập $0..5$, `parent = [0,1,2,3,4,5]`, `rank = [0,0,0,0,0,0]`.
>   * *Bước 1, 2, 3:* `union(0,1)`, `union(2,3)`, `union(1,2)` ghép dần các nhóm lại.
>   * *Bước 4 (Highlight Xanh - Path Compression):* Gọi `connected(0, 3)`. Trong hàm `find(3)`, nút 3 được nén nối thẳng về Gốc 0. `parent[3]` lập tức đổi thành 0!
>   * *Bước 6 (Highlight Tím - Tăng Rank):* `union(3, 5)` gộp 2 nhóm có cùng `rank = 1` $\to$ `rank[0]` tăng lên thành 2.

**🎙️ Lời thoại thuyết minh (Trà):**
> *"Để minh họa trực quan quá trình tự biến đổi này, xin mời Thầy và các bạn quan sát Bảng mô phỏng vết (Trace Table) trên Slide 18:*
>
> * Ban đầu ở **Bước 0**, ta có 6 phần tử độc lập với `parent[i] = i` và toàn bộ `rank = 0`.
> * Hãy chú ý ở **Bước 4 (Dòng màu xanh dương)**: Khi ta gọi lệnh kiểm tra liên thông `connected(0, 3)`, hàm `find(3)` được kích hoạt. Nhờ cơ chế **Path Compression**, con trỏ của nút 3 lập tức được nén nối thẳng về Gốc 0 (`parent[3] = 0`).
> * Và ở **Bước 6 (Dòng màu tím)**: Khi thực hiện `union(3, 5)`, vì hai nhóm có cùng Rank bằng 1, thuật toán chọn Gốc 0 làm đại diện chung và tự động nâng `rank[0]` lên mức 2.
>
> *Bảng Trace đã chứng minh rõ ràng cơ chế tự động giữ phẳng cây và bảo toàn chiều cao tối ưu của thuật toán DSU!"*

---

### 📍 SLIDE 19: BẪY CÀI ĐẶT, UNION BY SIZE & THUẬT TOÁN KRUSKAL (MST)
* **Thời lượng:** 55 giây.
* **Hành động trình chiếu:** Chuyển Slide 19. Chỉ vào hộp cảnh báo "Bẫy Rank sau nén", công thức Union by Size và ứng dụng Kruskal.

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **Bẫy cài đặt kinh điển (Trap):** Khi dùng Path Compression, chiều cao thực tế của cây bị giảm đi (ép phẳng), nhưng ta **không cập nhật lại mảng `rank[]`** vì làm thế sẽ mất thêm thời gian. Vì vậy, `rank` lúc này chỉ là *Upper Bound (chặn trên)* chứ không còn là chiều cao thực tế nữa!
> * **Biến thể Union by Size:** Thay vì quản lý `rank`, ta lưu mảng `size[]` đếm số lượng phần tử của cây. Có một mẹo cực hay trong C++: Lưu `size` dạng số âm ngay trong mảng `parent[]` (nếu `parent[root] < 0` thì `-parent[root]` chính là size của cây) $\to$ Tiết kiệm thêm 1 mảng phụ!
> * **Thuật toán Kruskal:** Thuật toán kinh điển tìm Cây khung nhỏ nhất (Minimum Spanning Tree - MST). Sắp xếp $E$ cạnh tốn $O(E \log E)$. Sau đó duyệt qua từng cạnh, dùng DSU để kiểm tra xem 2 đỉnh có tạo thành chu trình hay không (`find(u) != find(v)`). Nếu không tạo chu trình thì gọi `union(u, v)`. Nhờ DSU chạy $O(1)$, tổng thời gian Kruskal đạt mức tối ưu $O(E \log E)$!

**🎙️ Lời thoại thuyết minh (Trà):**
> *"Khi lập trình DSU trong thực tế, có một bẫy kỹ thuật rất quan trọng cần lưu ý:*
> * Sau khi Path Compression ép phẳng cây, chiều cao thực tế đã giảm xuống, nhưng mảng `rank` **không hề được cập nhật lại** vì chi phí tính toán lại chiều cao rất đắt. Do đó, `rank` chỉ đóng vai trò là một chặn trên xấp xỉ.
> * Một phương án thay thế rất được ưa chuộng là **Union by Size** — theo dõi trực tiếp số lượng phần tử của mỗi cây, thậm chí có thể lưu trực tiếp số âm vào mảng `parent` để tiết kiệm tối đa bộ nhớ RAM.
>
> *Và ứng dụng đỉnh cao nhất của DSU chính là **Thuật toán Kruskal** tìm Cây khung nhỏ nhất (MST) trên đồ thị:*
> * Ta sắp xếp $E$ cạnh theo trọng số tăng dần: Tốn $O(E \log E)$.
> * Sau đó duyệt từng cạnh, dùng `find()` của DSU để phát hiện chu trình trong $O(1)$. Nếu hai đỉnh chưa liên thông, ta nạp cạnh đó vào cây khung bằng lệnh `union()`.
>
> *Nhờ DSU, thuật toán Kruskal vận hành với tốc độ cực nhanh $O(E \log E)$!"*

---

### 📍 SLIDE 20: BẢNG ĐỐI SÁNH HIỆU NĂNG DSU VS GRAPH BFS/DFS
* **Thời lượng:** 40 giây.
* **Hành động trình chiếu:** Chuyển Slide 20. Đối chiếu các cột DSU vs Graph BFS/DFS vs Ma trận kề. Kết thúc Phần II và chuyển giao diễn giả.

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **So sánh toàn diện:**
>   * *Đồ thị BFS/DFS:* Thêm cạnh $O(1)$, nhưng truy vấn liên thông tốn $O(V + E)$, bộ nhớ $O(V + E)$.
>   * *Ma trận kề (Adjacency Matrix):* Truy vấn liên thông vẫn tốn $O(V)$, bộ nhớ tốn kém $O(V^2)$.
>   * *DSU:* Thêm cạnh $O(\alpha(V)) \approx O(1)$, Truy vấn liên thông $O(\alpha(V)) \approx O(1)$, Bộ nhớ siêu nhẹ đúng $O(V)$!

**🎙️ Lời thoại thuyết minh (Trà):**
> *"Nhìn vào Bảng đối sánh tổng hợp trên Slide 20, chúng ta thấy rõ sự áp đảo của DSU trong bài toán liên thông:*
> * Nếu dùng **BFS hay DFS**, mỗi thao tác truy vấn liên thông tiêu tốn $O(V + E)$ thời gian.
> * Nếu dùng **Ma trận kề**, bộ nhớ bị lãng phí tới $O(V^2)$ và thời gian vẫn là $O(V)$.
> * Trong khi đó, **DSU áp đảo hoàn toàn**: Thêm cạnh tốn $O(1)$, truy vấn liên thông tốn $O(1)$, và bộ nhớ chỉ tiêu tốn đúng một mảng tuyến tính $O(V)$!
>
> *Đó là sức mạnh phi thường của Cấu trúc Union-Find.*
>
> *Sau đây, để đúc kết lại toàn bộ bài học, giới thiệu Khung quyết định thiết kế hệ thống và các biến thể nâng cao, em xin kính mời bạn **Huỳnh Thị Thùy Trang** tiếp tục phần thuyết trình!"*

---

# 📕 PHẦN 3: KHUNG QUYẾT ĐỊNH, KIẾN TRÚC HỆ THỐNG & TỔNG KẾT
> **Diễn giả:** Huỳnh Thị Thùy Trang (MSSV: 25110371)  
> **Thời lượng dự kiến:** 4 phút 00 giây (Slide 21 – Slide 23)

---

### 📍 SLIDE 21: TECHNICAL DECISION FRAMEWORK
* **Thời lượng:** 55 giây.
* **Hành động trình chiếu:** Trang bước lên tự tin, mỉm cười chào Thầy và các bạn. Bật Slide 21. Chỉ vào Sơ đồ phân nhánh Cây Quyết Định (Decision Tree).

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **Khung tư duy kỹ thuật (Decision Framework):** Khi đối mặt với một bài toán thực tế, làm sao kỹ sư biết nên dùng cấu trúc dữ liệu nào?
>   1. *Bài toán yêu cầu tra cứu từ khóa chính xác (Exact Key Lookup)?* $\to$ **Hash Table** (nhanh nhất, $O(1)$).
>   2. *Bài toán cần tìm kiếm theo tiền tố chuỗi, gợi ý từ khóa (Prefix / Autocomplete)?* $\to$ **Trie** ($O(L)$).
>   3. *Bài toán cần quản lý tập hợp động, kiểm tra liên thông, chu trình đồ thị (Dynamic Connectivity / Cycles)?* $\to$ **Union-Find / DSU** ($O(\alpha(N))$).
>   4. *Bài toán cần tìm đường đi ngắn nhất hoặc duyệt đồ thị tĩnh có hướng (Shortest Path / Directed Graph)?* $\to$ **Graph BFS/DFS / Dijkstra**.

**🎙️ Lời thoại thuyết minh (Trang):**
> *"Xin cảm ơn phần trình bày rất sâu sắc của bạn Thanh Trà.*
>
> *Kính chào Thầy Vũ Đình Bảo cùng toàn thể các bạn, em tên là Huỳnh Thị Thùy Trang. Em xin phép được đại diện nhóm trình bày phần tổng kết chuyên đề với trọng tâm: **Khung Quyết Định Kỹ Thuật (Technical Decision Framework) và Kiến Trúc Hệ Thống**.*
>
> *Một kỹ sư phần mềm xuất sắc không phải là người biết nhiều cấu trúc dữ liệu phức tạp, mà là người biết **chính xác khi nào nên dùng cấu trúc nào**.*
>
> *Trên Slide 21 là Sơ đồ cây quyết định được nhóm chúng em đúc kết:*
> * Nếu bài toán chỉ yêu cầu tra cứu từ khóa chính xác mà không quan tâm thứ tự $\to$ Hãy chọn **Hash Table** để đạt $O(1)$ đơn giản và tối ưu bộ nhớ.
> * Nếu bài toán yêu cầu xử lý chuỗi, tìm kiếm tiền tố hoặc tự động gợi ý từ $\to$ **Trie** là giải pháp số 1 không thể thay thế.
> * Nếu bài toán thuộc dạng quan hệ tương đương, gộp nhóm động hoặc phát hiện chu trình trên đồ thị vô hướng $\to$ Hãy chọn **Union-Find (DSU)** để đạt tốc độ tức thì $O(1)$.
> * Còn nếu bài toán yêu cầu tìm đường đi ngắn nhất hoặc xử lý đồ thị có hướng phức tạp $\to$ Khi đó chúng ta mới cần đến **BFS, DFS hoặc Dijkstra**."*

---

### 📍 SLIDE 22: BÀI HỌC CỐT LÕI VỀ KIẾN TRÚC HỆ THỐNG
* **Thời lượng:** 50 giây.
* **Hành động trình chiếu:** Chuyển Slide 22. Nhấn mạnh 3 khối bài học cốt lõi: Query Pattern, Trade-offs và Hardware-awareness.

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **3 Định luật Kiến trúc:**
>   1. **"Query Pattern Drives Structure":** Cấu trúc dữ liệu phải phục vụ mẫu truy vấn của người dùng, không phải chiều ngược lại.
>   2. **"No Free Lunch — Time vs Space Trade-off":** Đổi không gian lấy thời gian (như Trie tốn RAM để đổi lấy tra cứu $O(L)$) hoặc nén dữ liệu để tiết kiệm RAM.
>   3. **"Hardware Awareness":** Viết code trong thế kỷ 21 phải hiểu CPU Cache, Spatial Locality và Pointer Chasing.

**🎙️ Lời thoại thuyết minh (Trang):**
> *"Từ việc nghiên cứu chuyên sâu Chương 15, nhóm chúng em xin đúc kết **3 bài học kiến trúc cốt lõi** mang tính nền tảng cho mọi kỹ sư phần mềm:*
>
> 1. **Thứ nhất: Mẫu Truy Vấn Quyết Định Cấu Trúc Dữ Liệu!** Không có cấu trúc dữ liệu nào là 'tốt nhất' cho mọi tình huống. Hiệu năng cao chỉ đạt được khi hình học của cấu trúc dữ liệu khớp hoàn hảo với luồng truy vấn của bài toán.
> 2. **Thứ hai: Quy luật Đánh đổi (Trade-off) Không Thể Tránh Khỏi!** Để đạt được tốc độ tìm kiếm tiền tố siêu nhanh $O(L)$, Trie đã chấp nhận đánh đổi thêm bộ nhớ con trỏ. Kỹ sư giỏi là người biết cân bằng giữa giới hạn phần cứng và yêu cầu thời gian phản hồi của sản phẩm.
> 3. **Thứ ba: Tư duy Tối ưu Phần cứng (Hardware-awareness)!** Lý thuyết Big-O là chưa đủ. Một cấu trúc dữ liệu thực chiến phải tận dụng được CPU Cache Locality và giảm thiểu hiện tượng Pointer Chasing trên bộ nhớ RAM."*

---

### 📍 SLIDE 23: CẤU TRÚC NÂNG CAO & LỜI KẾT Q&A
* **Thời lượng:** 55 giây.
* **Hành động trình chiếu:** Chuyển Slide 23. Điểm qua các biến thể mở rộng (Radix Tree, TST, Persistent DSU). Cúi đầu cảm ơn và mời Thầy cùng cả lớp đặt câu hỏi phản biện.

> 🧠 **BỔ NGHĨA DÀNH CHO NGƯỜI THUYẾT TRÌNH (Hiểu bản chất):**
> * **Mở rộng kiến thức nâng cao (Gây ấn tượng mạnh với Giảng viên):**
>   * *Radix Tree (Compressed Trie):* Nén các nút đơn thành chuỗi dài (được dùng trong Linux Kernel IP Routing).
>   * *Ternary Search Tree (TST):* Mỗi nút chỉ có 3 nhánh (`<`, `=`, `>`), kết hợp sức mạnh của BST và Trie, tiết kiệm 80% RAM.
>   * *Aho-Corasick:* Kết hợp Trie + KMP để tìm kiếm đồng thời hàng ngàn từ khóa trong văn bản.
>   * *Rollback DSU / Persistent DSU:* Cho phép quay ngược lịch sử thao tác gộp (Undo `union`) trong các bài toán đồ thị động nâng cao.

**🎙️ Lời thoại thuyết minh (Trang):**
> *"Để mở rộng nghiên cứu sau chuyên đề hôm nay, chúng ta có thể tiếp cận những biến thể nâng cao rất mạnh mẽ:*
> * Với Trie: Chúng ta có **Radix Tree** nén các chuỗi nút đơn được sử dụng trong Linux Kernel; **Ternary Search Tree (TST)** tiết kiệm tới 80% bộ nhớ; hay thuật toán **Aho-Corasick** tìm kiếm đồng thời hàng ngàn từ khóa trong văn bản.
> * Với DSU: Chúng ta có **Rollback DSU** và **Persistent DSU** cho phép quay lui thời gian và truy vấn lịch sử đồ thị trong các hệ thống phức tạp.
>
> *Kính thưa Thầy Vũ Đình Bảo cùng toàn thể các bạn sinh viên,*
> *Bài báo cáo chuyên đề Chương 15 của Nhóm DASA230179_06 đến đây xin phép được khép lại. Nhóm em xin chân thành cảm ơn Thầy và các bạn đã chú ý lắng nghe!*
>
> *Sau đây, nhóm chúng em rất mong nhận được những nhận xét đóng góp quý báu và các câu hỏi phản biện từ Thầy và cả lớp ạ!"*

---

# 🎯 BỘ CÂU HỎI PHẢN BIỆN DỰ PHÒNG CHUYÊN SÂU (Q&A DEFENSE)
*(Dành cho cả 3 thành viên tự tin bảo vệ bài báo cáo trước Giảng viên và Sinh viên)*

---

### ❓ Câu hỏi 1 (Về Trie - Tối ưu bộ nhớ):
**Giảng viên hỏi:** *"Trong cài đặt `TrieNode`, nếu ta có một tập dữ liệu văn bản tiếng Việt Unicode hoặc từ điển chứa hàng triệu từ, mảng `children[26]` sẽ không hoạt động được hoặc gây lãng phí bộ nhớ khủng khiếp. Các em sẽ giải quyết bài toán này như thế nào trong thực tế?"*

* **Diễn giả trả lời (Nhi / Trang):**
  > *"Dạ thưa Thầy, đối với tập ký tự lớn như Unicode tiếng Việt hoặc khi dữ liệu rất thưa thớt, chúng em có 3 giải pháp kỹ thuật cụ thể:*
  > 1. *Thay thế mảng tĩnh bằng `std::unordered_map<char32_t, TrieNode*>` hoặc `std::map`. Cách này chỉ cấp phát ô nhớ cho các ký tự thực sự xuất hiện, giúp tiết kiệm bộ nhớ tối đa.*
  > 2. *Chuyển đổi sang cấu trúc **Ternary Search Tree (TST)**: Mỗi nút chỉ duy trì đúng 3 con trỏ (`left`, `equal`, `right`), giúp hỗ trợ mọi tập ký tự mà dung lượng bộ nhớ chỉ tương đương một cây nhị phân.*
  > 3. *Sử dụng **Radix Tree (Compressed Trie)**: Nén toàn bộ các chuỗi nút con đơn lẻ không phân nhánh thành một nút duy nhất chứa một chuỗi con (substring), triệt tiêu các nút rác trung gian ạ."*

---

### ❓ Câu hỏi 2 (Về DSU - Chi tiết thuật toán & Ackermann):
**Giảng viên hỏi:** *"Nếu một lập trình viên chỉ cài đặt Path Compression mà KHÔNG dùng Union by Rank, thì độ phức tạp lý thuyết của DSU là bao nhiêu? Tại sao lại cần kết hợp cả hai?"*

* **Diễn giả trả lời (Trà / Trang):**
  > *"Dạ thưa Thầy:*
  > * *Nếu chỉ sử dụng duy nhất **Path Compression** mà không dùng Union by Rank, độ phức tạp trung bình (amortized) cho $M$ thao tác trên $N$ phần tử là **$O(M \log_{1 + M/N} N)$**, và trong trường hợp xấu nhất cho một thao tác đơn lẻ vẫn có thể chạm $O(\log N)$.*
  > * *Nếu chỉ sử dụng duy nhất **Union by Rank** mà không có Path Compression, độ phức tạp là **$O(\log N)$** trong trường hợp xấu nhất.*
  > * *Chỉ khi **kết hợp đồng thời cả Union by Rank và Path Compression**, cấu trúc cây vừa được khống chế chiều cao cơ sở, vừa liên tục được ép phẳng sau mỗi lần truy vấn, từ đó mới đạt được giới hạn tối ưu tuyệt đối **$O(M \alpha(N))$** theo chứng minh của Tarjan ạ."*

---

### ❓ Câu hỏi 3 (Về DSU - Bẫy cài đặt Rank):
**Giảng viên hỏi:** *"Sau khi hàm `find()` thực hiện nén đường đi (Path Compression), chiều cao của cây rõ ràng đã giảm xuống. Tại sao trong mã nguồn các em không trừ bớt giá trị của `rank` đi?"*

* **Diễn giả trả lời (Trà):**
  > *"Dạ thưa Thầy, đây chính là một điểm rất tinh tế trong thiết kế giải thuật DSU:*
  > * *Để tính toán lại chính xác chiều cao của một cây sau khi nén đường đi, chúng ta buộc phải duyệt qua toàn bộ các nút con của cây đó — thao tác này sẽ tốn chi phí thời gian lên tới $O(K)$ (với $K$ là số nút trong cây).*
  > * *Nếu làm như vậy, chúng ta sẽ tự phá hủy mục tiêu tốc độ $O(1)$ của hàm `find()`.*
  > * *Do đó, trong thuật toán DSU chuẩn, `rank` được định nghĩa là **chặn trên xấp xỉ (Upper Bound)** của chiều cao thay vì chiều cao chính xác. Việc giữ nguyên `rank` không làm ảnh hưởng đến tính đúng đắn của giải thuật mà vẫn đảm bảo thời gian chạy tối ưu tuyệt đối ạ."*

---

### ❓ Câu hỏi 4 (Về Kiến trúc & Hệ thống thực tế):
**Giảng viên hỏi:** *"Tại sao trong các bài toán đồ thị có trọng số tìm đường đi ngắn nhất (Shortest Path), người ta không dùng DSU mà phải dùng Dijkstra hay Bellman-Ford?"*

* **Diễn giả trả lời (Trang / Trà):**
  > *"Dạ thưa Thầy:*
  > * *Bản chất của DSU là cấu trúc dữ liệu quản lý **Quan hệ Tương đương (Equivalence Relation)** — nó chỉ trả lời được câu hỏi nhị phân: 'Hai đỉnh này có thuộc cùng một thành phần liên thông hay không?' (Yes/No Connectivity).*
  > * *DSU không lưu trữ thông tin về đường đi cụ thể, không lưu trọng số lũy kế giữa các chặng, và không duy trì hướng của đồ thị.*
  > * *Vì vậy, đối với bài toán tìm đường đi ngắn nhất có xét trọng số cạnh, chúng ta bắt buộc phải sử dụng các thuật toán duyệt đồ thị chuyên biệt như **Dijkstra** hoặc **Bellman-Ford** ạ."*

---

## 📋 CHECKLIST CHUẨN BỊ TRƯỚC GIỜ LÊN BÁO CÁO CHO 3 THÀNH VIÊN

1. **Chuẩn bị Kỹ thuật & Slide:**
   - [x] Mở sẵn file [index.html](file:///c:/Users/Admin/Documents/Workspace/DSA_15/index.html) trên trình duyệt Chrome/Edge, nhấn phím `F` để vào chế độ Fullscreen của Reveal.js.
   - [x] Thử bấm phím `Space` hoặc mũi tên `->` để đảm bảo hiệu ứng chuyển slide hoạt động mượt mà.
   - [x] Kiểm tra hiển thị công thức toán học KaTeX ($\alpha(N), O(L), O(N \log N)$) rõ nét.

2. **Phân chia vị trí đứng trên sân khấu:**
   - **Nhi:** Đứng phía bên trái màn chiếu, tay cầm bút laser, mở đầu chương trình từ Slide 00 đến Slide 11.
   - **Trà:** Đứng sẵn sàng, bước lên đổi chỗ nhẹ nhàng ở Slide 12, thuyết trình từ Slide 12 đến Slide 20.
   - **Trang:** Bước lên ở Slide 21, thuyết trình Slide 21 đến Slide 23 và chủ trì phần chào kết & điều phối Q&A.

3. **Nguyên tắc thuyết trình tự tin:**
   - Không đọc vẹt từng chữ trên slide — Nhìn vào các tiêu đề và biểu đồ để giải thích theo ý hiểu bản chất.
   - Sử dụng tay trỏ vào các bảng Big-O, dòng code C++ và hình minh họa để dẫn dắt ánh nhìn của Thầy và các bạn.
   - Nói to, rõ ràng, phát âm chuẩn các thuật ngữ: *Trie (phát âm là "try"), Disjoint-Set Union (DSU), Path Compression, Inverse Ackermann*.
