import matplotlib.pyplot

def plot_pc_arrays(pc_arrays):
    xs = pc_arrays[0]["X"]
    ys = pc_arrays[0]["Y"]
    zs = pc_arrays[0]["Z"]

    fig = matplotlib.pyplot.figure(figsize=(12,7))
    ax = fig.add_subplot(projection="3d")
    img = ax.scatter(xs, ys, zs, c=zs, cmap="viridis")
    fig.colorbar(img, label="Elevation")

    ax.view_init(30, 45)
    ax.set_xlabel("Easting")
    ax.set_ylabel("Northing")
    ax.set_title("Point Cloud Extract")


    matplotlib.pyplot.show()

def plot_2d_matrix(matrix):
    fig = matplotlib.pyplot.figure(figsize=(12,7))
    ax = fig.add_subplot()

    ax.matshow(matrix, cmap='viridis')

    # x y points
    # img = ax.scatter(grid["x"], grid["y"], c=grid["z"], cmap="viridis")
    # fig.colorbar(img, label="Elevation")

    ax.set_xlabel("Easting")
    ax.set_ylabel("Northing")
    ax.set_title("Point Cloud Extract")

    matplotlib.pyplot.show()

def save_matrix_image(matrix, outfile):
    fig = matplotlib.pyplot.figure(figsize=(12,7))
    ax = fig.add_subplot()

    ax.matshow(matrix, cmap='viridis')

    matplotlib.pyplot.axis('off')
    matplotlib.pyplot.savefig(outfile)