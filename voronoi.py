import pandas as pd
from scipy.spatial import Voronoi

input_file = r"C:\Users\bdeer\Desktop\Centres docents.csv"
df = pd.read_csv(input_file)

points = df[['Coordenades UTM X', 'Coordenades UTM Y']].values

vor = Voronoi(points)

voronoi_data = []
for region_index in vor.regions:
    if len(region_index) > 0 and -1 not in region_index:
        region_points = [vor.vertices[i] for i in region_index]
        for point in region_points:
            voronoi_data.append({
                'Polygon ID': len(voronoi_data) + 1,
                'Vertex X': point[0],
                'Vertex Y': point[1]
            })

df_voronoi = pd.DataFrame(voronoi_data)

df_voronoi.to_csv('Centres docents_voronoi_polygons.csv', index=False)