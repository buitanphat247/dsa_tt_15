import os, glob

workspace = r"C:\Users\Admin\Documents\Workspace\DSA_15"
slides_dir = os.path.join(workspace, "slides")
slides_1based_dir = os.path.join(workspace, "slides_1based")

# Shift existing slide_22 -> slide_23 down to slide_01 -> slide_02
for i in range(22, 0, -1):
    old_file = os.path.join(slides_dir, f"slide_{i:02d}.html")
    new_file = os.path.join(slides_dir, f"slide_{i+1:02d}.html")
    if os.path.exists(old_file):
        os.rename(old_file, new_file)

# Shift slides_1based
for i in range(23, 1, -1):
    old_file = os.path.join(slides_1based_dir, f"slide_{i:02d}.html")
    new_file = os.path.join(slides_1based_dir, f"slide_{i+1:02d}.html")
    if os.path.exists(old_file):
        os.rename(old_file, new_file)

agenda_content = """<section data-transition="slide">
    <div class="badge">Nội Dung Báo Cáo</div>
    <h2 style="font-size: 1.35em; margin-bottom: 24px;">
        <span class="text-gradient">MỤC LỤC CHUYÊN ĐỀ</span>
    </h2>

    <div class="grid-2" style="max-width: 1040px; margin: 0 auto; gap: 20px;">
        <!-- Phần 1 -->
        <div class="glass-card" style="text-align: left; padding: 18px 22px; border-left: 4px solid var(--accent-cyan);">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
                <span style="background: #e0f2fe; color: #0284c7; font-weight: 800; padding: 4px 10px; border-radius: 8px; font-size: 0.7em;">PHẦN I</span>
                <h3 style="font-size: 0.85em; margin: 0; color: #0f172a;">Đặt Vấn Đề & Giới Hạn</h3>
            </div>
            <ul style="font-size: 0.58em; margin: 0; padding-left: 18px; color: #475569;">
                <li>Giới hạn hiệu năng của BST & Hash Table ($O(\log N)$, Hash Collision)</li>
                <li>Thách thức trong hệ thống xử lý chuỗi & tập hợp quy mô lớn</li>
            </ul>
        </div>

        <!-- Phần 2 -->
        <div class="glass-card" style="text-align: left; padding: 18px 22px; border-left: 4px solid var(--accent-blue);">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
                <span style="background: #dbeafe; color: #1d4ed8; font-weight: 800; padding: 4px 10px; border-radius: 8px; font-size: 0.7em;">PHẦN II</span>
                <h3 style="font-size: 0.85em; margin: 0; color: #0f172a;">Cấu Trúc Dữ Liệu Trie</h3>
            </div>
            <ul style="font-size: 0.58em; margin: 0; padding-left: 18px; color: #475569;">
                <li>Nguyên lý Prefix Tree, Thao tác $O(L)$ độc lập quy mô dữ liệu</li>
                <li>Ứng dụng Autocomplete, Kiểm tra chính tả & Tối ưu bộ nhớ</li>
            </ul>
        </div>

        <!-- Phần 3 -->
        <div class="glass-card" style="text-align: left; padding: 18px 22px; border-left: 4px solid var(--accent-violet);">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
                <span style="background: #f3e8ff; color: #6b21a8; font-weight: 800; padding: 4px 10px; border-radius: 8px; font-size: 0.7em;">PHẦN III</span>
                <h3 style="font-size: 0.85em; margin: 0; color: #0f172a;">Cấu Trúc Union-Find (DSU)</h3>
            </div>
            <ul style="font-size: 0.58em; margin: 0; padding-left: 18px; color: #475569;">
                <li>Quản lý tập hợp rời rạc, Kỹ thuật Union by Rank & Path Compression</li>
                <li>Tối ưu tiệm cận thời gian thực $O(\\alpha(N))$ (Inverse Ackermann)</li>
            </ul>
        </div>

        <!-- Phần 4 -->
        <div class="glass-card" style="text-align: left; padding: 18px 22px; border-left: 4px solid var(--accent-emerald);">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
                <span style="background: #d1fae5; color: #047857; font-weight: 800; padding: 4px 10px; border-radius: 8px; font-size: 0.7em;">PHẦN IV</span>
                <h3 style="font-size: 0.85em; margin: 0; color: #0f172a;">Thực Nghiệm & Tổng Kết</h3>
            </div>
            <ul style="font-size: 0.58em; margin: 0; padding-left: 18px; color: #475569;">
                <li>Thử nghiệm Benchmark so sánh trên mã nguồn C++</li>
                <li>Tổng kết ứng dụng thực tế (IP Routing, MST Kruskal) & Q&A</li>
            </ul>
        </div>
    </div>

    <aside class="notes">
        Sau đây em xin đi qua tổng quan nội dung báo cáo ngày hôm nay. Bài thuyết trình được chia làm 4 phần chính: 
        Phần 1 phân tích các điểm nghẽn hiệu năng của cấu trúc dữ liệu truyền thống. 
        Phần 2 đi sâu vào Trie - giải pháp tối ưu cho xử lý chuỗi và tìm kiếm tiền tố. 
        Phần 3 trình bày Union-Find với thuật toán nén đường đi đạt tốc độ gần như tức thì. 
        Cuối cùng, Phần 4 minh chứng kết quả bằng benchmark mã nguồn C++ thực tế và ứng dụng thực tiễn.
    </aside>
</section>"""

# Write slide_01.html in slides/
with open(os.path.join(slides_dir, "slide_01.html"), "w", encoding="utf-8") as f:
    f.write(agenda_content.strip())

# Write slide_02.html in slides_1based/
with open(os.path.join(slides_1based_dir, "slide_02.html"), "w", encoding="utf-8") as f:
    f.write(agenda_content.strip())

print("Successfully inserted slide_01.html (Agenda Slide) and renumbered files!")
