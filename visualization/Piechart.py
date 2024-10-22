import plotly.graph_objects as go

# Data contoh
labels = ['MICE','Perikanan', 'Transportasi', 'Kesehatan', 'Hiburan','Perkebunan']
values = [31, 24, 18, 15,12]

# Membuat grafik lingkaran
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

# Menambahkan judul
fig.update_layout(title='Kategori Bidang Izin yang Dominan')

# Menampilkan plot
fig.show()