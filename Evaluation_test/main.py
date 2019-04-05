from modules.dataset import HDF5,scipy_filter
from modules import fetch,timestamp,utils
import os


URL = 'https://cernbox.cern.ch/index.php/s/wk7SN1qt2O7jbrl/download?x-access-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkcm9wX29ubHkiOmZhbHNlLCJleHAiOiIyMDE5LTA0LTAyVDA5OjIxOjAzLjE2NzIxNTI5KzAyOjAwIiwiZXhwaXJlcyI6MCwiaWQiOiIxNjgwMjkiLCJpdGVtX3R5cGUiOjAsIm10aW1lIjoxNTUyMDc0ODAzLCJvd25lciI6InNnZXNzIiwicGF0aCI6ImVvc2hvbWUtczozMDk1NjA4MzM1NDc5NjAzMiIsInByb3RlY3RlZCI6ZmFsc2UsInJlYWRfb25seSI6dHJ1ZSwic2hhcmVfbmFtZSI6IjE1NDE5NjIxMDg5MzUwMDAwMDBfMTY3XzgzOC5oNSIsInRva2VuIjoid2s3U04xcXQyTzdqYnJsIn0.vTSHovP3p4TFnjCTYrOebn6DqzLK8_3738juzZiXViw'

data_dir = 'data'
features_dir = 'features'
images_dir = 'images'

utils.make_dirs(data_dir,'a')
utils.make_dirs(features_dir,'a')
utils.make_dirs(images_dir,'a')


fetch.fromURL(URL, data_dir)



path='/AwakeEventData/XMPP-STREAK/StreakImage/streakImageData'
heightpath='/AwakeEventData/XMPP-STREAK/StreakImage/streakImageHeight'
widthpath='/AwakeEventData/XMPP-STREAK/StreakImage/streakImageWidth'



for root, dirs, files in os.walk(data_dir):
    for f in files:

        data = HDF5(os.path.join(root,f))

        ns = int(f.split('_')[0]) // 1e9
        tz_UTC = timestamp.convert_to_tz(ns,zone='UTC')
        tz_CERN = timestamp.convert_to_tz(ns,zone='CET')

        print('\ndatetime of hd5 \n  UTC: %s \n  CERN: %s'% (str(tz_UTC), str(tz_CERN)))

        data.export_features(features_dir)
        data.export_image(images_dir, path, heightpath, widthpath, filter = scipy_filter)
        



