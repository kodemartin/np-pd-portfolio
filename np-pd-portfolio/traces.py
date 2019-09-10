import numpy as np


def get_traces(grid, line, distance):
    """Given a planar grid of geometrical points
    find all points that are located within
    the specified distance from the line.

    :param grid: A sequence of tuples with the planar
        coordinates of the grid points.
    :param line: A sequence of the tuples with the
        boundary points on the reference line
    :param float distance: The distance from the line
        that defines the proximity area
    :rtype: numpy.array
    """
    grid = np.array(grid)
    line = np.array(line)
    # We define a local coordinate system
    # starting from one of the boundary
    # points of the reference line
    local_origin = np.array(line[0])

    # We find the vector representing the reference
    # line on the local coordinate system
    local_line = line - local_origin

    # We find the projection factors of the grid points
    # onto the reference line in the local system
    target_vector = local_line[1] - local_line[0]
    length = np.linalg.norm(target_vector)
    local_grid = grid - local_origin

    projection_factors = np.einsum('...j, j', local_grid, target_vector/length)
    # Find index of points that have a projection within
    # the boundary of the line
    pindex = (projection_factors >= 0) & (projection_factors <= length)

    projections = (local_origin +
                   projection_factors[pindex].reshape(-1, 1) *
                   target_vector.reshape(1, -1)/length)
    distances = grid[pindex] - projections

    trace_index = np.linalg.norm(distances, axis=1) <= distance

    return grid[pindex][trace_index]
