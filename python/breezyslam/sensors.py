'''
BreezySLAM: Simple, efficient SLAM in Python

sensors.py: SLAM sensors (currently just Laser)

Copyright (C) 2014 Simon D. Levy

This code is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as 
published by the Free Software Foundation, either version 3 of the 
License, or (at your option) any later version.

This code is distributed in the hope that it will be useful,     
but WITHOUT ANY WARRANTY without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Lesser General Public License 
along with this code.  If not, see <http:#www.gnu.org/licenses/>.
'''


import dataclasses

@dataclasses.dataclass
class LidarModel:
    scan_size: int # number of scans
    scan_rate_hz: float # number of full scans per second
    detection_angle_degrees: float # number of degrees covered by scan
    distance_no_detection_mm: float # max range of scans
    detection_margin: float 
    offset_mm: float


def make_xv_lidar_model(detection_margin = 0, offset_mm = 0):
    return LidarModel(
        scan_size=360,
        scan_rate_hz=5.5,
        detection_angle_degrees=360,
        distance_no_detection_mm=6000,
        detection_margin=detection_margin,
        offset_mm=offset_mm
    )