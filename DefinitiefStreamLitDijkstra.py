from PIL import ImageDraw
import time
import streamlit as st
from PIL import Image


class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # For undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def dijkstra(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        previous = [None] * self.size
        distances = [float('inf')] * self.size
        distances[start_vertex] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            if u is None:
                break

            visited[u] = True

            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt
                        previous[v] = u

        return distances, previous


g = Graph(58)

# Lokalen
g.add_vertex_data(0, 'A1')
g.add_vertex_data(1, 'A2')
g.add_vertex_data(2, 'A3')
g.add_vertex_data(3, 'A4')
g.add_vertex_data(4, 'B1')
g.add_vertex_data(5, 'B2')
g.add_vertex_data(6, 'B3')
g.add_vertex_data(7, 'B4')
g.add_vertex_data(8, 'C1')
g.add_vertex_data(9, 'C2')
g.add_vertex_data(10, 'C3')
g.add_vertex_data(11, 'C4')
g.add_vertex_data(12, 'C5')
g.add_vertex_data(13, 'C6')
g.add_vertex_data(14, 'C7')
g.add_vertex_data(15, 'D1')
g.add_vertex_data(16, 'D2')
g.add_vertex_data(17, 'H1')
g.add_vertex_data(18, 'G1')
g.add_vertex_data(19, 'OLC')
g.add_vertex_data(20, 'Aula')

# Lokalen-gang knooppunten
g.add_vertex_data(21, 'A1g')
g.add_vertex_data(22, 'A2g')
g.add_vertex_data(23, 'A3g')
g.add_vertex_data(24, 'A4g')
g.add_vertex_data(25, 'B1g')
g.add_vertex_data(26, 'B2g')
g.add_vertex_data(27, 'B3g')
g.add_vertex_data(28, 'B4g')
g.add_vertex_data(29, 'C1g')
g.add_vertex_data(30, 'C2g')
g.add_vertex_data(31, 'C3g')
g.add_vertex_data(32, 'C4g')
g.add_vertex_data(33, 'C5g')
g.add_vertex_data(34, 'C6g')
g.add_vertex_data(35, 'C7g')
g.add_vertex_data(36, 'D1g')
g.add_vertex_data(37, 'D2g')
g.add_vertex_data(38, 'H1g')
g.add_vertex_data(39, 'G1g')
g.add_vertex_data(40, 'OLCg')
g.add_vertex_data(41, 'Aulag')

# Gangknooppunten
g.add_vertex_data(42, 'gang1')
g.add_vertex_data(43, 'gang2')
g.add_vertex_data(44, 'gang3')
g.add_vertex_data(45, 'gang4')
g.add_vertex_data(46, 'gang5')
g.add_vertex_data(47, 'gang6')
g.add_vertex_data(48, 'gang7')
g.add_vertex_data(49, 'gang8')
g.add_vertex_data(50, 'gang9')
g.add_vertex_data(51, 'gang10')
g.add_vertex_data(52, 'gang11')
g.add_vertex_data(53, 'gang12')
g.add_vertex_data(54, 'gang13')
g.add_vertex_data(55, 'gang14')
g.add_vertex_data(56, 'gang15')
g.add_vertex_data(57, 'kluisjes')

# coordinaten
coordinates = {
    "A1": (1150, 750),
    "A2": (1150, 850),
    "A3": (1150, 975),
    "A4": (1150, 1060),
    "B1": (960, 600),
    "B2": (900, 600),
    "B3": (840, 600),
    "B4": (750, 600),
    "C1": (420, 800),
    "C2": (420, 875),
    "C3": (420, 950),
    "C4": (420, 1050),
    "C5": (550, 1120),
    "C6": (550, 1080),
    "C7": (590, 975),
    "D1": (1400, 500),
    "D2": (1400, 400),
    "H1": (425, 525),
    "G1": (250, 400),
    "OLC": (590, 750),
    "Aula": (925, 450),
    "A1g": (1215, 750),
    "A2g": (1215, 850),
    "A3g": (1215, 975),
    "A4g": (1215, 1060),
    "B1g": (960, 550),
    "B2g": (900, 550),
    "B3g": (840, 550),
    "B4g": (750, 550),
    "C1g": (475, 800),
    "C2g": (475, 875),
    "C3g": (475, 950),
    "C4g": (475, 1050),
    "C5g": (475, 1120),
    "C6g": (475, 1080),
    "C7g": (590, 910),
    "D1g": (1430, 500),
    "D2g": (1430, 400),
    "H1g": (425, 460),
    "G1g": (250, 510),
    "OLCg": (590, 680),
    "Aulag": (925, 350),
    "gang1": (1215, 625),
    "gang2": (1150, 625),
    "gang3": (1150, 550),
    "gang4": (1075, 550),
    "gang5": (1075, 450),
    "gang6": (1075, 350),
    "gang7": (730, 350),
    "gang8": (730, 460),
    "gang9": (590, 460),
    "gang10": (590, 550),
    "gang11": (475, 680),
    "gang12": (475, 910),
    "gang13": (325, 460),
    "gang14": (325, 510),
    "gang15": (1430, 550),
    "kluisjes": (1075, 200)
}

# Lokalen tot hun gangknooppunten
g.add_edge(0, 21, 300)   # A1 - A1g, afstand 300
g.add_edge(1, 22, 515)   # A2 - A2g, afstand 515
g.add_edge(2, 23, 550)   # A3 - A3g, afstand 550
g.add_edge(3, 24, 540)   # A4 - A4g, afstand 540
g.add_edge(4, 25, 350)   # B1 - B1g, afstand 350
g.add_edge(5, 26, 350)   # B2 - B2g, afstand 350
g.add_edge(6, 27, 350)   # B3 - B3g, afstand 350
g.add_edge(7, 28, 350)   # B4 - B4g, afstand 350
g.add_edge(8, 29, 350)   # C1 - C1g, afstand 350
g.add_edge(9, 30, 350)   # C2 - C2g, afstand 350
g.add_edge(10, 31, 350)   # C3 - C3g, afstand 350
g.add_edge(11, 32, 350)   # C4 - C4g, afstand 350
g.add_edge(12, 33, 500)   # C5 - C5g, afstand 500
g.add_edge(13, 34, 400)   # C6 - C6g, afstand 400
g.add_edge(14, 35, 410)   # C7 - C7g, afstand 410
g.add_edge(15, 36, 450)   # D1 - D1g, afstand 450
g.add_edge(16, 37, 450)   # D2 - D2g, afstand 450
g.add_edge(17, 38, 575)   # H1 - H1g, afstand 575
g.add_edge(18, 39, 1100)  # G1 - G1g, afstand 1100
g.add_edge(19, 40, 480)   # OLC - OLCg, afstand 480
g.add_edge(20, 41, 725)   # Aula - Aulag, afstand 725
g.add_edge(20, 46, 1225)  # Aula - gang5, afstand 1225

# Lokalen-gang tot overige knooppunten
g.add_edge(21, 22, 1125)  # A1g - A2g, afstand 1125
g.add_edge(21, 42, 825)   # A1g - gang1, afstand 825
g.add_edge(22, 23, 860)   # A2g - A3g, afstand 860
g.add_edge(23, 24, 700)   # A3g - A4g, afstand 700
g.add_edge(25, 26, 530)   # B1g - B2g, afstand 530
g.add_edge(25, 45, 830)   # B1g - gang4, afstand 830
g.add_edge(26, 27, 560)   # B2g - B3g, afstand 560
g.add_edge(27, 28, 560)   # B3g - B4g, afstand 560
g.add_edge(28, 51, 1475)  # B4g - gang10, afstand 1475
g.add_edge(29, 30, 666)   # C1g - C2g, afstand 666
g.add_edge(29, 52, 840)   # C1g - gang11, afstand 840
g.add_edge(30, 53, 400)   # C2g - gang12, afstand 400
g.add_edge(31, 32, 775)   # C3g - C4g, afstand 775
g.add_edge(31, 53, 350)   # C3g - gang12, afstand 350
g.add_edge(32, 34, 315)   # C4g - C6g, afstand 315
g.add_edge(33, 34, 270)   # C5g - C6g, afstand 270
g.add_edge(35, 53, 870)   # C7g - gang12, afstand 870
g.add_edge(36, 37, 700)   # D1g - D2g, afstand 700
g.add_edge(36, 56, 725)   # D1g - gang15, afstand 725
g.add_edge(38, 50, 1475)  # H1g - gang9, afstand 1475
g.add_edge(38, 54, 675)   # H1g - gang13, afstand 675
g.add_edge(39, 55, 550)   # G1g - gang14, afstand 550
g.add_edge(40, 51, 1080)  # OLCg - gang10, afstand 1080
g.add_edge(40, 52, 930)   # OLCg - gang11, afstand 930
g.add_edge(41, 47, 1225)  # Aulag - gang6, afstand 1225
g.add_edge(41, 48, 1500)  # Aulag - gang7, afstand 1500

# Gangknooppunten onderling
g.add_edge(42, 43, 540)   # gang1 - gang2, afstand 540
g.add_edge(43, 44, 635)   # gang2 - gang3, afstand 635
g.add_edge(44, 45, 690)   # gang3 - gang4, afstand 690
g.add_edge(44, 56, 2330)  # gang3 - gang15, afstand 2330
g.add_edge(45, 46, 850)   # gang4 - gang5, afstand 850
g.add_edge(46, 47, 750)   # gang5 - gang6, afstand 750
g.add_edge(48, 49, 890)   # gang7 - gang8, afstand 890
g.add_edge(49, 50, 1250)  # gang8 - gang9, afstand 1250
g.add_edge(50, 51, 725)   # gang9 - gang10, afstand 725
g.add_edge(54, 55, 400)   # gang13 - gang14, afstand 400
g.add_edge(57, 47, 15000)  # kluisjes - gang6, afstand 15000


# Start- en eindpunt selecteren
start_vertex = st.selectbox("Select starting point:", g.vertex_data)
end_vertex = st.selectbox("Select end point:", g.vertex_data)

# foto laten zien
img = Image.open(
    "D:\RoutePlanner dingen\Plattegronden\BeganeGrondChristelijkLyceumGoed.png")
endpoint_img = Image.open("D:\Coding\PWS\endpoint.png")
# st.image(img, width=1000, caption="Plattegrond begane grond")

if st.button("Find Shortest Path"):
    start_time = time.time()
    distances, previous = g.dijkstra(start_vertex)
    end_time = time.time()

    # Pad reconstrueren
    end_index = g.vertex_data.index(end_vertex)
    path = []
    current = end_index
    while current is not None:
        path.append(g.vertex_data[current])
        current = previous[current]
    path.reverse()

    # Resultaat tonen
    st.write(f"**Shortest path:** {' → '.join(path)}")
    st.write(f"**Distance:** {distances[end_index]} cm")
    st.write(f"**Walking time:** {distances[end_index] / 112:.1f} s")
    st.write(f"**Calculation time:** {(end_time - start_time)*1000:.3f} ms")

    draw = ImageDraw.Draw(img)

    for i in range(len(path) - 1):
        p1 = coordinates[path[i]]
        p2 = coordinates[path[i + 1]]
        draw.line([p1, p2], fill="red", width=5)

        # Resize endpoint icoon
    new_width = 30
    w_percent = new_width / endpoint_img.width
    new_height = int(endpoint_img.height * w_percent)
    endpoint_img = endpoint_img.resize(
        (new_width, new_height), Image.Resampling.LANCZOS)

    # Plaats het icoon exact op het eindpunt
    x, y = coordinates[path[-1]]
    y -= 15
    top_left = (x - new_width // 2, y - new_height // 2)
    img.paste(endpoint_img, top_left, endpoint_img)  # transparantie behouden

st.image(img, width=1000, caption="Kortste route")
# st.image(img2, width=20)

# Python
