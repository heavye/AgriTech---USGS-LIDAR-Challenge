import pdal
import json

PUBLIC_DATA_PATH = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"
# IA_FullState
REGION = 'USGS_LPC_CO_SoPlatteRiver_Lot5_2013_LAS_2015/'
# ([minx, maxx], [miny, maxy])
# "([-10425171.940, -10423171.940], [5164494.710, 5166494.710])"
BOUNDS = "([-11669524.7, -11666600.8], [4776607.3, 4778714.4])"
PUBLIC_ACCESS_PATH = PUBLIC_DATA_PATH + REGION + "ept.json"
OUTPUT_FILENAME_LAZ = "laz/SoPlatteRiver.laz"
OUTPUT_FILENAME_TIF = "tif/SoPlatteRiver.tif"
PIPELINE_PATH = 'get_data.json'


def get_raster_terrain(bounds: str, region: str, PUBLIC_ACCESS_PATH: str = PUBLIC_ACCESS_PATH,
                       OUTPUT_FILENAME_LAZ: str = OUTPUT_FILENAME_LAZ, OUTPUT_FILENAME_TIF: str = OUTPUT_FILENAME_TIF,
                       PIPELINE_PATH: str = PIPELINE_PATH) -> None:
    # print(BOUNDS) 

    with open(PIPELINE_PATH) as json_file:
        the_json = json.load(json_file)


    the_json['pipeline'][0]['bounds'] = bounds
    the_json['pipeline'][0]['filename'] = PUBLIC_ACCESS_PATH
    the_json['pipeline'][3]['filename'] = OUTPUT_FILENAME_LAZ
    the_json['pipeline'][4]['filename'] = OUTPUT_FILENAME_TIF

    pipeline = pdal.Pipeline(json.dumps(the_json))
    
    try:
    
        pipe_exec = pipeline.execute()
        metadata = pipeline.metadata
        # print('metadata', metadata)
        # log = pipeline.log
        # print('logs', log)
    
    except RuntimeError as e:
        print(e)
        # RuntimeError: filters.hag: Input PointView does not have any points classification as ground
        print('RunTime Error, writing 0s and moving to next bounds')
        pass
    
    if __name__ == "__main__":
        get_raster_terrain(bounds=BOUNDS, region=REGION)
