# Points adında elemanları tuple olan bir list oluşturuyoruz.
points = [(3, 4), (5, 7), (2, 8), (9, 6)]


# İki nokta arasındaki mesafeyi ölçmek istiyoruz bu yüzden euclideanDistance adında bir fonksiyon oluşturuyoruz.
def euclideanDistance(coordinate1, coordinate2):
    return pow(pow(coordinate1[0] - coordinate2[0], 2) + pow(coordinate1[1] - coordinate2[1], 2), 0.5)


# Mesafeleri tutması için boş bir list tanımlıyoruz.
distance = []
# Mesafeleri hesaplamak için bir döngü kuruyoruz.
for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        distance.append(euclideanDistance(points[i], points[j]))
# Minimum mesafeyi bulmak için bir tane daha for döngüsü kullanıyoruz.
min_distance = distance[0]  # ilk mesafeyi başlangıç olarak kabul ediyoruz.
for dist in distance[1:]:  # ilk mesafeyi zaten aldık o yüzden indexi 1 den başlatıyoruz.
    if dist < min_distance:
        min_distance = dist
print("Minimum mesafe:", min_distance)

