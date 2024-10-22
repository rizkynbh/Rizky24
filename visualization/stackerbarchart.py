import plotly.graph_objects as go

# Data untuk diagram batang
categories = ['2022', '2023']
values_A = [63, 71,]
values_B = [37, 29,]


# Membuat diagram batang horizontal bertumpuk
fig = go.Figure()

fig.add_trace(go.Bar(
    y=categories,  # Untuk diagram horizontal, gunakan 'y' sebagai kategori
    x=values_A,  # 'x' menjadi nilai yang diplot ke sumbu horizontal
    name='Perusahaan',
    orientation='h'
))

fig.add_trace(go.Bar(
    y=categories,
    x=values_B,
    name='Individu',
    orientation='h'
))

# Update layout untuk mengatur tampilan diagram batang bertumpuk horizontal
fig.update_layout(
    barmode='stack',  # Mengatur mode stack
    title='Tipe Pemohon',
    xaxis_title='Perbandingan Dalam Persen (%)',
    yaxis_title='Tahun',
    xaxis=dict(range=[0, 100])  # Membuat sumbu x dari 0 ke 100%
)

# Menampilkan diagram
fig.show()
