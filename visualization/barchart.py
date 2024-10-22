import plotly.graph_objects as go

# Data contoh
categories = ['A', 'B', 'C', 'D']
values = [12, 15, 7, 20]

# Membuat grafik batang
fig = go.Figure(data=[go.Bar(x=categories, y=values)])

# Menambahkan judul dan label
fig.update_layout(title='Grafik Batang Contoh',
                  xaxis_title='Kategori',
                  yaxis_title='Nilai')

# Menampilkan plot
fig.show()