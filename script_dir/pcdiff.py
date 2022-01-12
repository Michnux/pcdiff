import open3d as o3d
import numpy as np
import laspy
from matplotlib import cm



def pcdiff(input_path, ref_path, work_dir, max_dist):

	fi = laspy.read(input_path)
	x = fi.X * fi.header.scales[0] + fi.header.offsets[0]
	y = fi.Y * fi.header.scales[1] + fi.header.offsets[1]
	z = fi.Z * fi.header.scales[2] + fi.header.offsets[2]
	xyz = np.vstack([x.astype(np.float32), y.astype(np.float32), z.astype(np.float32)]).transpose()

	fr = laspy.read(ref_path)
	xr = fr.X * fr.header.scales[0] + fr.header.offsets[0]
	yr = fr.Y * fr.header.scales[1] + fr.header.offsets[1]
	zr = fr.Z * fr.header.scales[2] + fr.header.offsets[2]
	xyz_ref = np.vstack([xr.astype(np.float32), yr.astype(np.float32), zr.astype(np.float32)]).transpose()

	pcd = o3d.geometry.PointCloud()
	pcd.points = o3d.utility.Vector3dVector(xyz)

	pcd_ref = o3d.geometry.PointCloud()
	pcd_ref.points = o3d.utility.Vector3dVector(xyz_ref)

	dists = pcd.compute_point_cloud_distance(pcd_ref)
	dists = np.array(dists)
	dists = [min(dist, max_dist) for dist in dists]

	# dists = [0.5 for dist in dists]


	# cmap = cm.get_cmap('bwr')
	cmap = cm.get_cmap('jet')
	colors = [cmap(dist/max_dist)[0:3] for dist in dists]
	colors = np.array(colors)*(2**16-1)

	# local visualization (for debug purpose)
	# pcd_diff = o3d.geometry.PointCloud()
	# pcd_diff.points = o3d.utility.Vector3dVector(xyz)
	# pcd_diff.colors = o3d.utility.Vector3dVector(colors)
	# o3d.visualization.draw_geometries([pcd_diff])

	fi.red = colors[:,0]
	fi.green = colors[:,1]
	fi.blue = colors[:,2]
	fi.intensity = dists
	fi.write(work_dir+'output.las')



if __name__ == "__main__":

	input_path = '../work_dir/sampled point cloud.las'
	ref_path = '../work_dir/Point Cloud.las'
	work_dir = '../work_dir/'
	pcdiff(input_path, ref_path, work_dir, 1.0)