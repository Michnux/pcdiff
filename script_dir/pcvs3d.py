import open3d as o3d
import numpy as np
import laspy
from matplotlib import cm



def pcvs3d():

	f = laspy.read('../work_dir/input.las')
	# f = laspy.read('./210323_Vol_6_Lidar.las')
	# print(f.header.__dict__)
	scale = f.header.scale
	offset = f.header.offset
	mins = f.header.mins
	maxs = f.header.maxs

	print('scale', scale)
	print('offset', offset)

	# print(f.header.vlrs)
	# for i in range(len(f.header.vlrs)):
	# 	print(f.header.vlrs[i].__dict__)

	x = f.X * f.header.scales[0] + f.header.offsets[0]
	y = f.Y * f.header.scales[1] + f.header.offsets[1]
	z = f.Z * f.header.scales[2] + f.header.offsets[2]


	# min_x = mins[0]
	# min_y = mins[1]
	# max_x = maxs[0]
	# max_y = maxs[1]

	# min_x = min(x)
	# min_y = min(y)
	# max_x = max(x)
	# max_y = max(y)
	xyz = np.vstack([x.astype(np.float32), y.astype(np.float32), z.astype(np.float32)]).transpose()

	# xyz = xyz[0:1000]


	# print(xyz)

	pcd = o3d.geometry.PointCloud()
	pcd.points = o3d.utility.Vector3dVector(xyz)

	# o3d.visualization.draw_geometries([pcd])


	xyz_ref = xyz+[0,0,0.1]

	pcd_ref = o3d.geometry.PointCloud()


	pcd_ref.points = o3d.utility.Vector3dVector(xyz_ref)


	dists = pcd_ref.compute_point_cloud_distance(pcd)
	# print(dists)
	dists = np.array(dists)
	dists = dists/max(dists)

	cmap = cm.get_cmap('RdYlGn', 12)
	colors = [cmap(dist)[0:3] for dist in dists]
	# print(colors)

	pcd_diff = o3d.geometry.PointCloud()
	pcd_diff.points = o3d.utility.Vector3dVector(xyz)
	pcd_diff.colors = o3d.utility.Vector3dVector(colors)

	o3d.visualization.draw_geometries([pcd_diff])


if __name__ == "__main__":

	pcvs3d()