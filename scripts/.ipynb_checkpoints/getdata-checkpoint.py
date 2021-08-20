
import pdal
import json
                                                                                                            

data_path = "https://s3-us-west-2-amazonaws.com/usgs-lidar-public"
region = 'USGS_LPC_CO_SoPlatteRiver_Lot5_2013_LAS_2015/'
bound = "([-93.756155, 41.918015, -93.747334, 41.921429])"
public_access_path = data_path + region + "ept.json"
output_flename_laz = "laz/SoPlatteRiver.laz"
output_flename_tif = "tif/SoPlatteRiver.tif"
pipline_path = "get_data.json"

#region and boundary
output_flename_laz = "laz/SoPlatteRiver.laz"
def get_raster_terrain(bounds:str,region:str, PUBLIC_ACCESS_PATH:str = public_access_path ,OUTPUT_FILENAME_LAZ:str =                                        output_flename_laz,
                    OUTPUT_FILENAME_TIF:str = output_flename_tif ,PIPLINE_PATH:str =pipline_path )->None:

    with open(PIPLINE_PATH) as json_file:
        the_json = json.load(json_file)

    the_json['pipline'][0]['bounds']= bounds
    the_json['pipline'][0]['filename']= PUBLIC_ACCESS_PATH
    the_json['pipline'][3]['filename']= OUTPUT_FILENAME_LAZ
    the_json['pipline'][4]['filename']= OUTPUT_FILENAME_TIF

    pipline = pdal.pipline(json.dumps(the_json))

    try:
        pipe_exec = pipline.execute()
        metadata=pipline.metadata
    except RuntimeError as e:
        print(e)


    if name== "main":
        get_raster_terrain(bounds=bound,region = region)