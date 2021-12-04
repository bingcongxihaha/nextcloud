# -*- coding: utf-8 -*-
import os
import argparse
from nextcloud import NextCloud


def initnxc():
    NEXTCLOUD_URL = "http://192.168.168.50:8080"
    NEXTCLOUD_USERNAME = "admin"
    NEXTCLOUD_PASSWORD = "admin"
    to_js = True
    nxc = NextCloud(endpoint=NEXTCLOUD_URL, user=NEXTCLOUD_USERNAME,
                    password=NEXTCLOUD_PASSWORD, json_output=to_js)
# 获取用户的列表
    a = nxc.get_users()
    #print(a.data)
# 获取用户的文件夹信息
    #c = nxc.list_folders('admin')
    # print(c.data)
    return nxc
# 上传


def upload():
    nxc = initnxc()
    u=nxc.upload_file('admin', local_filepath, upload_filepath)
    print(u)

# 下载


def download():
    try:
        if os.path.exists(download_file):
            print(download_file+" is exists")
        else:
            nxc.download_file('admin', download_filepath)
            if os.path.exists(download_file):
                print(download_file+" is download success")
            else:
                print(download_file+" is download fail")
    except Exception as e:
        print('Error:', e)

# 分享图片拿到公共链接


def share():
    nxc = initnxc()
    d = nxc.create_share('miner_directory/b.log', 3)
    print(d.data['url'])


if __name__ == '__main__':
    nxc = initnxc()
    parser = argparse.ArgumentParser(description='upload to fileServer or download to localPath...')
    parser.add_argument('--upload', default=False, type=str, help='upload')
    parser.add_argument('--download', default=False, type=str,help='download')
    args = parser.parse_args()
    if args.upload:
        if args.download:
            parser.error("不支持同时上传、下载，详见--help")
        else:
            local_filepath = str(args.upload)
            upload_file = "%s" % local_filepath
            upload_filepath = 'miner_directory/%s' % upload_file
            upload()
    elif args.download:
        if args.upload:
            parser.error("don`t support，详见--help")
        else:
            local_filepath = str(args.download)
            download_file = "%s" % local_filepath
            download_filepath = 'miner_directory/%s' % download_file
            download()
    else:
        parser.error("no options，see --help")