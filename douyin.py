import contextlib
import json

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from util import logger

HOT_SEARCH_URL = 'https://aweme.snssdk.com/aweme/v1/hot/search/list/'
HOT_STAR_URL = 'https://aweme.snssdk.com/aweme/v1/hotsearch/star/billboard/'
HOT_LIVE_URL = 'https://webcast.amemv.com/webcast/ranklist/hot/'
BRAND_CATEGORY_URL = 'https://aweme.snssdk.com/aweme/v1/hotsearch/brand/category/'
HOT_BRAND_URL = 'https://aweme.snssdk.com/aweme/v1/hotsearch/brand/billboard/'
HOT_MUSIC_URL = 'https://aweme.snssdk.com/aweme/v1/chart/music/list/'

HEADERS = {
    'user-agent': 'okhttp3'
}
QUERIES = {
    'device_platform': 'android',
    'version_name': '13.2.0',
    'version_code': '130200',
    'aid': '1128'
}
RETRIES = Retry(total=3,
                backoff_factor=1,
                status_forcelist=[k for k in range(400, 600)])


@contextlib.contextmanager
def request_session():
    s = requests.session()
    try:
        s.headers.update(HEADERS)
        s.mount("http://", HTTPAdapter(max_retries=RETRIES))
        s.mount("https://", HTTPAdapter(max_retries=RETRIES))
        yield s
    finally:
        s.close()


class Douyin:

    def get_hot_social_search(self):
        url = 'https://www.douyin.com/aweme/v1/web/hot/search/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&detail_list=1&source=6&board_type=2&board_sub_type=4&type=13&update_version_code=170400&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=960&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=125.0.0.0&browser_online=true&engine_name=Blink&engine_version=125.0.0.0&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=6&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7256468520636220963&msToken=VCfAfz8pQ7PtVV_Cl-uz1qcStC9n2fhMZxNCEWB3zc00uSJqyTLEbktKjaIeOE1inLgOtB8dPo8VS7y1E7i4p4Ip8R5i145nsKDE3Dlt5IZ_O9F2b6pVsRUolsxEWxwxuw%3D%3D&a_bogus=x7W0QRgfdDDNfDWf552LfY3q6R33YDIn0CPYMD2fHxvOlL39HMTv9exYuTTvzujjNs%2FDIeSjy4hbT3ohrQIyMZwf9W0L%2F25kQfSkKl3pso0j53inCLf%2FE0iL5hsAtFH8svH4EKi8owVtSYLhWxAJ5kIlO62kFobyifELtXL%3D' \

        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'cookie':'store-region=cn-gd; store-region-src=uid; bd_ticket_guard_client_web_domain=2; my_rd=2; d_ticket=85f22704ec9a28086a24bb27b9d495fda3b1a; _bd_ticket_crypt_doamin=2; __security_server_data_status=1; ttwid=1%7CCqfHBi9iIjucrl-wf5fxqcmAf5T5hfEIO-E6dAnpU2A%7C1714961102%7Cf457efd7c374b907b774046d452a42a5e29403b4b2df61aead7d6a3f08cc2c8d; passport_assist_user=Cj1jStB5jfQ7pm9Wmt8w1Gm5dWr7H0PQDdBCOjGnwYQU12Lj9wkw_MtyHQeEC3H-r6M3a1XlR3ufKpaApob9GkoKPI6UWAKJ3p8Sr73Pt4DreGqKgipbz8tFYJ6f-jE8BRcjk0VVUWxqlTl22eKP59brQKSg207GIpP6K0KgfBCDldENGImv1lQgASIBA4jdYq8%3D; n_mh=bGsDnA5Qz6AKwhuAmIUxv97kwUeX3JiZdaauFZARHn8; sso_uid_tt=ac1424e9428cfd64ace025315a476897; sso_uid_tt_ss=ac1424e9428cfd64ace025315a476897; toutiao_sso_user=87cfd4a29a15136f9db62b922c1aa855; toutiao_sso_user_ss=87cfd4a29a15136f9db62b922c1aa855; sid_ucp_sso_v1=1.0.0-KGFkY2Y1NmQ2ZTViMWUxNjRmOTM5NDI0NjdlZWI5YWE3MWM2ODcxNmUKHwj-yOPimgMQtJqGsgYY7zEgDDDGw_bhBTgFQPsHSAMaAmxmIiA4N2NmZDRhMjlhMTUxMzZmOWRiNjJiOTIyYzFhYTg1NQ; ssid_ucp_sso_v1=1.0.0-KGFkY2Y1NmQ2ZTViMWUxNjRmOTM5NDI0NjdlZWI5YWE3MWM2ODcxNmUKHwj-yOPimgMQtJqGsgYY7zEgDDDGw_bhBTgFQPsHSAMaAmxmIiA4N2NmZDRhMjlhMTUxMzZmOWRiNjJiOTIyYzFhYTg1NQ; uid_tt=ebab2a7cff84a73811873d480c40bed9; uid_tt_ss=ebab2a7cff84a73811873d480c40bed9; sid_tt=921b91dc81f993ff737d3e8701ce085b; sessionid=921b91dc81f993ff737d3e8701ce085b; sessionid_ss=921b91dc81f993ff737d3e8701ce085b; LOGIN_STATUS=1; _bd_ticket_crypt_cookie=a81535aecbad7eeb7c86cb21c481ab63; s_v_web_id=verify_lwesljva_N4k1iSd8_wMMb_4w7P_96uN_dpXcdszl6CKx; publish_badge_show_info=%220%2C0%2C0%2C1718592059040%22; csrf_session_id=f3cca850a64f43485b6503db520bf9b2; sid_guard=921b91dc81f993ff737d3e8701ce085b%7C1718592060%7C5184000%7CFri%2C+16-Aug-2024+02%3A41%3A00+GMT; sid_ucp_v1=1.0.0-KGJkMTk4OWFkZDE2MjVkOTU4NWRhNzA5MjFhM2MyMDZiZTc5YzExZWQKGQj-yOPimgMQvMS-swYY7zEgDDgFQPsHSAQaAmhsIiA5MjFiOTFkYzgxZjk5M2ZmNzM3ZDNlODcwMWNlMDg1Yg; ssid_ucp_v1=1.0.0-KGJkMTk4OWFkZDE2MjVkOTU4NWRhNzA5MjFhM2MyMDZiZTc5YzExZWQKGQj-yOPimgMQvMS-swYY7zEgDDgFQPsHSAQaAmhsIiA5MjFiOTFkYzgxZjk5M2ZmNzM3ZDNlODcwMWNlMDg1Yg; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.403%7D; dy_swidth=1536; dy_sheight=960; strategyABtestKey=%221718592952.681%22; download_guide=%223%2F20240617%2F1%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAgUjAAzbkcpfPkZWWLoPEMQdS3_IwF3nTt0jjg0K1bIQ%2F1718640000000%2F0%2F0%2F1718616359011%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A960%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A6%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; douyin.com; device_web_cpu_core=6; device_web_memory_size=8; WallpaperGuide=%7B%22showTime%22%3A1718593164246%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A19%2C%22cursor2%22%3A0%2C%22hoverTime%22%3A1718603282019%7D; pwa2=%220%7C0%7C3%7C1%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAgUjAAzbkcpfPkZWWLoPEMQdS3_IwF3nTt0jjg0K1bIQ%2F1718640000000%2F1718615225071%2F1718615169293%2F0%22; xg_device_score=7.296312049014711; passport_fe_beating_status=true; SEARCH_RESULT_LIST_TYPE=%22single%22; __ac_nonce=066700d4e007927fd350f; __ac_signature=_02B4Z6wo00f01-znFbQAAIDBUWg-XazUfhfswxEAAJ1TnFGCqrKcOQr8c.RBZ2F.HO8CsaWQwc1EsBHvVoPYUtuN.7svy9lBY1.dNFWpaNaFVZ8d6mA.Qw452ivYRBpEe8Lfj72ZZHTSBTsy6c; home_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQ2NweWF4MWxnUyt3Z3phL0NWcmpDOGtkM0htRkVBTEppWHlYbFRsVHNaYkRrcGJ2YnRrelVwWTVqY3lWcGd6anJvaHduSXhHWks5WUhHVmlHWW5xK2c9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=rEO0jbj5DSR2pJ8CfekCx2WVMZHrZv-a9cCcOjg9pzmx8jNC4UmxCGTNLWTJb72FlkynZBRw7KPJ4xcQV72oVQW65WPHq3HGMqpa970nMBoQalMrn4fHy3g=; odin_tt=8a4570670e0c00bd7ad3c4b075a94fd6195fca2d9b7b36012946c96faa64c54abf78475818cb50a1b0a6600a96bd861f; IsDouyinActive=true',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
        }
        items = []
        resp = None
        try:
            with request_session() as s:
                resp = s.get(url, headers=headers)
                obj = json.loads(resp.text)
                word_list = obj['data']['word_list']
                items = [item for item in word_list]
        except:
            logger.exception('get hot search failed')
        return (items, resp)

    def get_hot_search(self):
        """热点
            {
                "word_cover": {
                    "uri": "tos-cn-p-0015/fd4bf2569c7b4991a5b21cb63c34789b",
                    "url_list": [
                        "https://p3-dy-ipv6.byteimg.com/img/tos-cn-p-0015/fd4bf2569c7b4991a5b21cb63c34789b~noop.jpeg?from=3218412987",
                        "https://p9-dy.byteimg.com/img/tos-cn-p-0015/fd4bf2569c7b4991a5b21cb63c34789b~noop.jpeg?from=3218412987",
                        "https://p29-dy.byteimg.com/img/tos-cn-p-0015/fd4bf2569c7b4991a5b21cb63c34789b~noop.jpeg?from=3218412987"
                    ]
                },
                "group_id": "6722307068134446350",
                "related_words": null,
                "hotlist_param": "{\"version\":1}",
                "label": 0,
                "challenge_id": "",
                "sentence_id": "211198",
                "drift_info": null,
                "position": 1,
                "word_type": 1,
                "event_time": 1610171248,
                "word": "山东高考听力",
                "hot_value": 8225483,
                "video_count": 4
            }
        """

        items = []
        resp = None
        try:
            with request_session() as s:
                resp = s.get(HOT_SEARCH_URL, params=QUERIES)
                obj = json.loads(resp.text)
                word_list = obj['data']['word_list']
                items = [item for item in word_list]
        except:
            logger.exception('get hot search failed')
        return (items, resp)

    def get_hot_star(self):
        """明星
        {
            "honor_tags": [
                2
            ],
            "user_info": {
                "nickname": "冯巩",
                "signature": "请大家多关注我！\n合作联系：侯先生 13146277832",
                "avatar_thumb": {
                    "uri": "100x100/314ed000225fde1f50b62",
                    "url_list": [
                        "https://p9-dy.byteimg.com/aweme/100x100/314ed000225fde1f50b62.jpeg?from=4010531038",
                        "https://p3-dy-ipv6.byteimg.com/aweme/100x100/314ed000225fde1f50b62.jpeg?from=4010531038",
                        "https://p26-dy.byteimg.com/aweme/100x100/314ed000225fde1f50b62.jpeg?from=4010531038"
                    ]
                },
                "status": 1,
                "user_rate": 1,
                "avatar_larger": {
                    "uri": "1080x1080/314ed000225fde1f50b62",
                    "url_list": [
                        "https://p1-dy-ipv6.byteimg.com/aweme/1080x1080/314ed000225fde1f50b62.jpeg?from=4010531038",
                        "https://p9-dy.byteimg.com/aweme/1080x1080/314ed000225fde1f50b62.jpeg?from=4010531038",
                        "https://p3-dy-ipv6.byteimg.com/aweme/1080x1080/314ed000225fde1f50b62.jpeg?from=4010531038"
                    ]
                },
                "sec_uid": "MS4wLjABAAAAh6tcornHHqhS6WdOvMvMJEsuMOgUjRpggx3BIBW6BFVVnSS2Gi3fahxR_Kkp1VY-",
                "uid": "1991933892508967"
            },
            "is_new": false,
            "rank_diff": 0,
            "hot_value_bar": 95,
            "sprint": {
                "sprint": 0,
                "followers": null
            },
            "hot_value": 18752181,
            "factor_hot_value": 4813294,
            "factor_interact_value": 13935024
        }
        """
        items = []
        resp = None
        try:
            with request_session() as s:
                resp = s.get(HOT_STAR_URL, params=QUERIES)
                obj = json.loads(resp.text)
                user_list = obj['user_list']
                items = [item for item in user_list]
        except:
            logger.exception('get hot star failed')
        return (items, resp)

    def get_hot_live(self):
        """直播
            {
                "user": {
                    "id": 52504997437,
                    "short_id": 10128106,
                    "nickname": "梦想山妹",
                    "gender": 2,
                    "signature": "下午四点❤️开播粉丝马甲梦之队\n多变才艺主播情感分享正能量\n只有这一个号，其他都是冒充，请勿上当受骗❗️❗️❗️",
                    "level": 1,
                    "birthday": 0,
                    "telephone": "",
                    "avatar_thumb": {
                        "url_list": [
                            "https://p3-dy-ipv6.byteimg.com/img/tos-cn-avt-0015/ba862483f84360f146d6a429d760a894~c5_100x100.jpeg?from=4010531038",
                            "https://p1-dy-ipv6.byteimg.com/img/tos-cn-avt-0015/ba862483f84360f146d6a429d760a894~c5_100x100.jpeg?from=4010531038",
                            "https://p29-dy.byteimg.com/img/tos-cn-avt-0015/ba862483f84360f146d6a429d760a894~c5_100x100.jpeg?from=4010531038"
                        ],
                        "uri": "100x100/tos-cn-avt-0015/ba862483f84360f146d6a429d760a894",
                        "height": 0,
                        "width": 0,
                        "avg_color": "",
                        "image_type": 0,
                        "open_web_url": "",
                        "is_animated": false
                    },
                    "avatar_medium": {
                        "url_list": [
                            "https://p29-dy.byteimg.com/img/tos-cn-avt-0015/ba862483f84360f146d6a429d760a894~c5_720x720.jpeg?from=4010531038",
                            "https://p9-dy.byteimg.com/img/tos-cn-avt-0015/ba862483f84360f146d6a429d760a894~c5_720x720.jpeg?from=4010531038",
                            "https://p3-dy-ipv6.byteimg.com/img/tos-cn-avt-0015/ba862483f84360f146d6a429d760a894~c5_720x720.jpeg?from=4010531038"
                        ],
                        "uri": "720x720/tos-cn-avt-0015/ba862483f84360f146d6a429d760a894",
                        "height": 0,
                        "width": 0,
                        "avg_color": "",
                        "image_type": 0,
                        "open_web_url": "",
                        "is_animated": false
                    },
                    "avatar_large": {
                        "url_list": [
                            "https://p3-dy-ipv6.byteimg.com/img/tos-cn-avt-0015/ba862483f84360f146d6a429d760a894~c5_1080x1080.jpeg?from=4010531038",
                            "https://p29-dy.byteimg.com/img/tos-cn-avt-0015/ba862483f84360f146d6a429d760a894~c5_1080x1080.jpeg?from=4010531038",
                            "https://p6-dy-ipv6.byteimg.com/img/tos-cn-avt-0015/ba862483f84360f146d6a429d760a894~c5_1080x1080.jpeg?from=4010531038"
                        ],
                        "uri": "1080x1080/tos-cn-avt-0015/ba862483f84360f146d6a429d760a894",
                        "height": 0,
                        "width": 0,
                        "avg_color": "",
                        "image_type": 0,
                        "open_web_url": "",
                        "is_animated": false
                    },
                    "verified": true,
                    "experience": 0,
                    "city": "邵阳",
                    "status": 1,
                    "create_time": 0,
                    "modify_time": 1610179364,
                    "secret": 0,
                    "share_qrcode_uri": "216a001514e5e371acee",
                    "income_share_percent": 0,
                    "badge_image_list": [
                        {
                            "url_list": [
                                "http://p3-webcast-dycdn.byteimg.com/img/webcast/user_grade_level_v3_34.png~tplv-obj.image",
                                "http://p9-webcast-dycdn.byteimg.com/img/webcast/user_grade_level_v3_34.png~tplv-obj.image",
                                "http://p6-webcast-dycdn.byteimg.com/img/webcast/user_grade_level_v3_34.png~tplv-obj.image"
                            ],
                            "uri": "webcast/user_grade_level_v3_34.png",
                            "height": 16,
                            "width": 32,
                            "avg_color": "",
                            "image_type": 1,
                            "open_web_url": "",
                            "is_animated": false
                        }
                    ],
                    "follow_info": {
                        "following_count": 415,
                        "follower_count": 1975706,
                        "follow_status": 0,
                        "push_status": 0
                    },
                    "pay_grade": {
                        "total_diamond_count": 180771,
                        "name": "",
                        "next_name": "",
                        "level": 34,
                        "next_diamond": 0,
                        "now_diamond": 0,
                        "this_grade_min_diamond": 170000,
                        "this_grade_max_diamond": 230000,
                        "pay_diamond_bak": 0,
                        "grade_describe": "距离35级还差4.9w抖币",
                        "grade_icon_list": [],
                        "screen_chat_type": 0,
                        "new_im_icon_with_level": {
                            "url_list": [
                                "http://p3-webcast-dycdn.byteimg.com/img/webcast/user_grade_level_v3_34.png~tplv-obj.image",
                                "http://p9-webcast-dycdn.byteimg.com/img/webcast/user_grade_level_v3_34.png~tplv-obj.image",
                                "http://p6-webcast-dycdn.byteimg.com/img/webcast/user_grade_level_v3_34.png~tplv-obj.image"
                            ],
                            "uri": "webcast/user_grade_level_v3_34.png",
                            "height": 16,
                            "width": 32,
                            "avg_color": "",
                            "image_type": 1,
                            "open_web_url": "",
                            "is_animated": false
                        },
                        "new_live_icon": {
                            "url_list": [
                                "http://p1-webcast-dycdn.byteimg.com/img/webcast/aweme_pay_grade_2x_30_34.png~tplv-obj.image",
                                "http://p9-webcast-dycdn.byteimg.com/img/webcast/aweme_pay_grade_2x_30_34.png~tplv-obj.image",
                                "http://p3-webcast-dycdn.byteimg.com/img/webcast/aweme_pay_grade_2x_30_34.png~tplv-obj.image"
                            ],
                            "uri": "webcast/aweme_pay_grade_2x_30_34.png",
                            "height": 12,
                            "width": 12,
                            "avg_color": "",
                            "image_type": 1,
                            "open_web_url": "",
                            "is_animated": false
                        },
                        "upgrade_need_consume": 0,
                        "next_privileges": "",
                        "score": 180771,
                        "grade_banner": ""
                    },
                    "fans_club": {
                        "data": {
                            "club_name": "",
                            "level": 0,
                            "user_fans_club_status": 0,
                            "badge": {
                                "icons": {
                                    "0": {
                                        "url_list": [],
                                        "uri": "",
                                        "height": 0,
                                        "width": 0,
                                        "avg_color": "",
                                        "image_type": 0,
                                        "open_web_url": "",
                                        "is_animated": false
                                    }
                                },
                                "title": ""
                            },
                            "available_gift_ids": [],
                            "anchor_id": 0
                        },
                        "prefer_data": {}
                    },
                    "special_id": "",
                    "real_time_icons": [],
                    "new_real_time_icons": [],
                    "top_vip_no": 0,
                    "user_attr": {
                        "is_muted": false,
                        "is_admin": false,
                        "is_super_admin": false,
                        "admin_privileges": []
                    },
                    "own_room": {
                        "room_ids": [
                            6915651327284480783
                        ],
                        "room_ids_str": [
                            "6915651327284480783"
                        ]
                    },
                    "pay_score": 180771,
                    "ticket_count": 25903325,
                    "link_mic_stats": 2,
                    "display_id": "mxsm7268",
                    "with_commerce_permission": true,
                    "with_fusion_shop_entry": true,
                    "total_recharge_diamond_count": 0,
                    "verified_content": "",
                    "top_fans": [],
                    "sec_uid": "MS4wLjABAAAArGN0fC3sMSzWq8kz_cpA1tlHtdWJAtpFU52YI2pD5R8",
                    "user_role": 0,
                    "authorization_info": 3,
                    "adversary_authorization_info": 3,
                    "media_badge_image_list": [],
                    "adversary_user_status": 0,
                    "commerce_webcast_config_ids": [],
                    "badge_image_list_v2": [
                        {
                            "url_list": [
                                "http://p3-webcast-dycdn.byteimg.com/img/webcast/user_grade_level_v3_34.png~tplv-obj.image",
                                "http://p9-webcast-dycdn.byteimg.com/img/webcast/user_grade_level_v3_34.png~tplv-obj.image",
                                "http://p6-webcast-dycdn.byteimg.com/img/webcast/user_grade_level_v3_34.png~tplv-obj.image"
                            ],
                            "uri": "webcast/user_grade_level_v3_34.png",
                            "height": 16,
                            "width": 32,
                            "avg_color": "",
                            "image_type": 1,
                            "open_web_url": "",
                            "is_animated": false
                        }
                    ],
                    "allow_be_located": false,
                    "allow_find_by_contacts": false,
                    "allow_others_download_video": false,
                    "allow_others_download_when_sharing_video": false,
                    "allow_share_show_profile": false,
                    "allow_show_in_gossip": false,
                    "allow_show_my_action": false,
                    "allow_strange_comment": false,
                    "allow_unfollower_comment": false,
                    "allow_use_linkmic": false,
                    "bg_img_url": "",
                    "birthday_description": "",
                    "birthday_valid": false,
                    "block_status": 0,
                    "comment_restrict": 0,
                    "constellation": "",
                    "disable_ichat": 0,
                    "enable_ichat_img": 0,
                    "exp": 0,
                    "fan_ticket_count": 0,
                    "fold_stranger_chat": false,
                    "follow_status": 0,
                    "hotsoon_verified": false,
                    "hotsoon_verified_reason": "",
                    "ichat_restrict_type": 0,
                    "id_str": "52504997437",
                    "is_follower": false,
                    "is_following": false,
                    "need_profile_guide": false,
                    "pay_scores": 0,
                    "push_comment_status": false,
                    "push_digg": false,
                    "push_follow": false,
                    "push_friend_action": false,
                    "push_ichat": false,
                    "push_status": false,
                    "push_video_post": false,
                    "push_video_recommend": false,
                    "verified_mobile": false,
                    "verified_reason": "",
                    "with_car_management_permission": false
                },
                "score": 1024549,
                "rank": 1,
                "gap_description": "",
                "raw_ad_data": "",
                "room": {
                    "id": 6915651327284480783,
                    "id_str": "6915651327284480783",
                    "title": "我来了",
                    "user_count": 63377,
                    "cover": {
                        "url_list": [
                            "http://p6-webcast-dycdn.byteimg.com/img/webcast/6912989390914505487~tplv-obj.image",
                            "http://p3-webcast-dycdn.byteimg.com/img/webcast/6912989390914505487~tplv-obj.image",
                            "http://p1-webcast-dycdn.byteimg.com/img/webcast/6912989390914505487~tplv-obj.image"
                        ],
                        "uri": "webcast/6912989390914505487",
                        "height": 0,
                        "width": 0,
                        "avg_color": "#89A37C",
                        "image_type": 0,
                        "open_web_url": "",
                        "is_animated": false
                    },
                    "challenge_info": "",
                    "content_label": {
                        "url_list": [
                            "http://p9-webcast-dycdn.byteimg.com/img/webcast/aweme_cover_redPackage_webcast_3_2.png~tplv-obj.image",
                            "http://p6-webcast-dycdn.byteimg.com/img/webcast/aweme_cover_redPackage_webcast_3_2.png~tplv-obj.image",
                            "http://p3-webcast-dycdn.byteimg.com/img/webcast/aweme_cover_redPackage_webcast_3_2.png~tplv-obj.image"
                        ],
                        "uri": "webcast/aweme_cover_redPackage_webcast_3_2.png",
                        "height": 0,
                        "width": 0,
                        "avg_color": "#A37C96",
                        "image_type": 0,
                        "open_web_url": "",
                        "is_animated": false
                    }
                },
                "label": "电商"
            }
        """
        items = []
        resp = None
        try:
            with request_session() as s:
                resp = s.get(HOT_LIVE_URL, params=QUERIES)
                obj = json.loads(resp.text)
                ranks = obj['data']['ranks']
                items = [item for item in ranks]
        except:
            logger.exception('get hot live failed')
        return (items, resp)

    def get_brand_category(self):
        """品牌分类
            {
                "id": 1,
                "name": "汽车"
            }
        """
        items = []
        resp = None
        try:
            with request_session() as s:
                resp = s.get(BRAND_CATEGORY_URL, params=QUERIES)
                obj = json.loads(resp.text)
                category_list = obj['category_list']
                items = [item for item in category_list]
        except:
            logger.exception('get brand category failed')
        return (items, resp)

    def get_hot_brand(self, category: int):
        """品牌榜
        {
            "interactive_tag_type": 0,
            "is_in_webcasting": false,
            "bluev_uid": "99808893411",
            "rank": 1,
            "name": "宝马",
            "logo_url": {
                "url_list": [
                    "https://p1.pstatp.com/large/web.business.image/202003165d0d22dc33f467844f859685"
                ],
                "uri": "https://p1.pstatp.com/large/web.business.image/202003165d0d22dc33f467844f859685"
            },
            "heat": 1252,
            "rank_diff": 0,
            "heat_diff": -14,
            "explain_tag_desc": "",
            "bluev_sec_uid": "MS4wLjABAAAAYd9-Fw6hyTIpS7RaLLpTLdmxmv0pmQczk9QAXC7uYso",
            "id": 7532
        }
        """
        items = []
        resp = None
        try:
            with request_session() as s:
                params = QUERIES.copy()
                params.update({'category_id': str(category)})
                resp = s.get(HOT_BRAND_URL, params=params)
                obj = json.loads(resp.text)
                brand_list = obj['brand_list']
                items = [item for item in brand_list]
        except:
            logger.exception('get hot brand failed')
        return (items, resp)

    def get_hot_music(self):
        """
            {
                "music_info": {
                    "album": "四季予你",
                    "cover_thumb": {
                    "width": 720,
                    "height": 720,
                    "uri": "iesmusic-cn-local/v1/tt-obj/image/c3297eb70e9c1abf01e07151fbeee2cd.jpg",
                    "url_list": [
                        "https://p9-dy.byteimg.com/aweme/100x100/iesmusic-cn-local/v1/tt-obj/image/c3297eb70e9c1abf01e07151fbeee2cd.jpg.jpeg",
                        "https://p6-dy-ipv6.byteimg.com/aweme/100x100/iesmusic-cn-local/v1/tt-obj/image/c3297eb70e9c1abf01e07151fbeee2cd.jpg.jpeg"
                    ]
                    },
                    "source_platform": 10036,
                    "is_restricted": false,
                    "is_video_self_see": false,
                    "play_url": {
                    "uri": "https://sf3-dycdn-tos.pstatp.com/obj/iesmusic-cn-local/v1/tt-obj/2241bef2d16820c170109557dbfd940c.mp3",
                    "url_list": [
                        "https://sf3-dycdn-tos.pstatp.com/obj/iesmusic-cn-local/v1/tt-obj/2241bef2d16820c170109557dbfd940c.mp3",
                        "https://sf6-dycdn-tos.pstatp.com/obj/iesmusic-cn-local/v1/tt-obj/2241bef2d16820c170109557dbfd940c.mp3"
                    ],
                    "width": 720,
                    "height": 720,
                    "url_key": "6907550512367864584"
                    },
                    "preview_start_time": 67.4,
                    "cover_large": {
                    "uri": "iesmusic-cn-local/v1/tt-obj/image/c3297eb70e9c1abf01e07151fbeee2cd.jpg",
                    "url_list": [
                        "https://p9-dy.byteimg.com/aweme/720x720/iesmusic-cn-local/v1/tt-obj/image/c3297eb70e9c1abf01e07151fbeee2cd.jpg.jpeg",
                        "https://p6-dy-ipv6.byteimg.com/aweme/720x720/iesmusic-cn-local/v1/tt-obj/image/c3297eb70e9c1abf01e07151fbeee2cd.jpg.jpeg"
                    ],
                    "width": 720,
                    "height": 720
                    },
                    "prevent_download": false,
                    "unshelve_countries": null,
                    "preview_end_time": 0,
                    "shoot_duration": 18,
                    "lyric_short_position": null,
                    "mute_share": false,
                    "tag_list": null,
                    "is_matched_metadata": false,
                    "is_audio_url_with_cookie": false,
                    "author": "程响",
                    "id_str": "6907550512367864584",
                    "collect_stat": 0,
                    "offline_desc": "",
                    "avatar_thumb": {
                    "uri": "2f8d90002d445edafadbe",
                    "url_list": [
                        "https://p9-dy.byteimg.com/aweme/100x100/2f8d90002d445edafadbe.jpeg?from=4010531038",
                        "https://p6-dy-ipv6.byteimg.com/aweme/100x100/2f8d90002d445edafadbe.jpeg?from=4010531038",
                        "https://p3-dy-ipv6.byteimg.com/aweme/100x100/2f8d90002d445edafadbe.jpeg?from=4010531038"
                    ],
                    "width": 720,
                    "height": 720
                    },
                    "matched_song": {
                    "title": "四季予你（剪辑版）",
                    "h5_url": "https://sf6-scmcdn-tos.pstatp.com/goofy/toutiao/canon/douyin/canon/index.html",
                    "cover_medium": {
                        "uri": "iesmusic-cn-local/v1/tt-obj/image/c3297eb70e9c1abf01e07151fbeee2cd.jpg",
                        "url_list": [
                        "https://p9.douyinpic.com/aweme/200x200/iesmusic-cn-local/v1/tt-obj/image/c3297eb70e9c1abf01e07151fbeee2cd.jpg.jpeg",
                        "https://p6-dy-ipv6.byteimg.com/aweme/200x200/iesmusic-cn-local/v1/tt-obj/image/c3297eb70e9c1abf01e07151fbeee2cd.jpg.jpeg",
                        "https://p3-dy-ipv6.byteimg.com/aweme/200x200/iesmusic-cn-local/v1/tt-obj/image/c3297eb70e9c1abf01e07151fbeee2cd.jpg.jpeg"
                        ],
                        "width": 720,
                        "height": 720
                    },
                    "id": "6909031453405923330",
                    "author": "程响"
                    },
                    "can_background_play": true,
                    "cover_medium": {
                    "uri": "iesmusic-cn-local/v1/tt-obj/image/c3297eb70e9c1abf01e07151fbeee2cd.jpg",
                    "url_list": [
                        "https://p9-dy.byteimg.com/aweme/200x200/iesmusic-cn-local/v1/tt-obj/image/c3297eb70e9c1abf01e07151fbeee2cd.jpg.jpeg",
                        "https://p6-dy-ipv6.byteimg.com/aweme/200x200/iesmusic-cn-local/v1/tt-obj/image/c3297eb70e9c1abf01e07151fbeee2cd.jpg.jpeg"
                    ],
                    "width": 720,
                    "height": 720
                    },
                    "binded_challenge_id": 0,
                    "music_chart_ranks": null,
                    "strong_beat_url": {
                    "uri": "https://sf-tk-sg.ibytedtos.com/obj/tiktok-obj/strong_beat/1687613061406721",
                    "url_list": [
                        "https://sf-tk-sg.ibytedtos.com/obj/tiktok-obj/strong_beat/1687613061406721"
                    ],
                    "width": 720,
                    "height": 720
                    },
                    "is_commerce_music": false,
                    "id": 6907550512367864584,
                    "dmv_auto_show": false,
                    "author_position": null,
                    "duration": 18,
                    "prevent_item_download_status": 0,
                    "extra": "{\"beats\":{},\"hotsoon_review_time\":-1,\"aggregate_exempt_conf\":[],\"has_edited\":0,\"review_unshelve_reason\":0,\"douyin_beats_info\":{},\"schedule_search_time\":0,\"music_label_id\":1257,\"reviewed\":1}",
                    "user_count": 662543,
                    "owner_handle": "",
                    "is_original": false,
                    "is_del_video": false,
                    "external_song_info": [],
                    "avatar_large": {
                    "uri": "2f8d90002d445edafadbe",
                    "url_list": [
                        "https://p26-dy.byteimg.com/aweme/1080x1080/2f8d90002d445edafadbe.jpeg?from=4010531038",
                        "https://p3-dy-ipv6.byteimg.com/aweme/1080x1080/2f8d90002d445edafadbe.jpeg?from=4010531038",
                        "https://p29-dy.byteimg.com/aweme/1080x1080/2f8d90002d445edafadbe.jpeg?from=4010531038"
                    ],
                    "width": 720,
                    "height": 720
                    },
                    "audition_duration": 18,
                    "position": null,
                    "reason_type": 0,
                    "title": "四季予你（剪辑版）",
                    "author_deleted": false,
                    "artists": [],
                    "cover_hd": {
                    "uri": "iesmusic-cn-local/v1/tt-obj/image/c3297eb70e9c1abf01e07151fbeee2cd.jpg",
                    "url_list": [
                        "https://p9-dy.byteimg.com/aweme/1080x1080/iesmusic-cn-local/v1/tt-obj/image/c3297eb70e9c1abf01e07151fbeee2cd.jpg.jpeg",
                        "https://p6-dy-ipv6.byteimg.com/aweme/1080x1080/iesmusic-cn-local/v1/tt-obj/image/c3297eb70e9c1abf01e07151fbeee2cd.jpg.jpeg"
                    ],
                    "width": 720,
                    "height": 720
                    },
                    "status": 1,
                    "owner_nickname": "",
                    "mid": "6907550512367864584",
                    "avatar_medium": {
                    "uri": "2f8d90002d445edafadbe",
                    "url_list": [
                        "https://p6-dy-ipv6.byteimg.com/aweme/720x720/2f8d90002d445edafadbe.jpeg?from=4010531038",
                        "https://p1.douyinpic.com/aweme/720x720/2f8d90002d445edafadbe.jpeg?from=4010531038",
                        "https://p29-dy.byteimg.com/aweme/720x720/2f8d90002d445edafadbe.jpeg?from=4010531038"
                    ],
                    "width": 720,
                    "height": 720
                    },
                    "is_original_sound": false
                },
                "heat": 17611210,
                "can_background_play": true,
                "has_copyright": true
            }
        """
        items = []
        resp = None
        try:
            with request_session() as s:
                params = QUERIES.copy()
                params.update(
                    {'chart_id': '6853972723954146568', 'count': '100'})
                resp = s.get(HOT_MUSIC_URL, params=params)
                obj = json.loads(resp.text)
                music_list = obj['music_list']
                items = [item for item in music_list]
        except:
            logger.exception('get hot music failed')
        return (items, resp)


if __name__ == "__main__":
    dy = Douyin()
    # items, text = dy.get_brand_category()
    # logger.info('len:%s items:%s', len(items), items[-1])

    items, text = dy.get_hot_brand(category=10)
    for item in items:
        logger.info('item:%s', item)

    # items, text = dy.get_hot_music()
    # logger.info('len:%s items:%s', len(items), items[0])
