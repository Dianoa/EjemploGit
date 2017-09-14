import geopandas as gpd

DIRECTORIO_SHAPE = '/media/dianvla/Libelle/Curso_Python/destdv1gw_c'
mx_boundary = gpd.GeoDataFrame.from_file(DIRECTORIO_SHAPE)

print(mx_boundary.__class__)
