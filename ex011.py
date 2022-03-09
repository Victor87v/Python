# Área pintada
l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
area = l * a
pintar = area/2
print('Sua parede de dimensão {}x{} tem a área de {}m²\ne precisará de {}l de tinta para ser pintada'.format(l,a,area,pintar))