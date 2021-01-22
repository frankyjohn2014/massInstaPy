from instapy import InstaPy
from instapy.util import smart_run


session = InstaPy(username="nail_design_blog", password="223221QWE").login()
with smart_run(session):

    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=500,
                                        min_followers=45,
                                    min_following=120)

    # session.set_dont_include(["friend1", "friend2", "friend3"])
    # session.set_dont_like(["pizza", "#store"])
    # session.unfollow_users(amount=10)
    # session.set_do_follow(enabled=True, percentage=10, times=2)
    # actions
    nailssoko = session.grab_followers(username="nails.so.ko", amount="full", live_match=True, store_locally=True)
    # session.follow_by_list(followlist=kolesnaya_nails_minsk, times=1, sleep_delay=600, interact=False)
    # session.follow_by_tags(["nails", "гельлак", "ногти", "nailart", "ногтиминск", "minsk", "аппаратныйманикюр", "beauty", "шеллак", "педикюр", "лайкзалайк", "лайкзалайки"], amount=10,randomize=True)
    # session.like_by_tags(["nails", "гельлак", "ногти", "nailart", "ногтиминск", "minsk", "аппаратныйманикюр", "beauty", "шеллак", "педикюр", "лайкзалайк", "лайкзалайки"], amount=10,randomize=True)
    # session.set_user_interact(amount=4,
    #                          percentage=50,
    #                          randomize=True,
    #                          media='Photo')
    # session.unfollow_users(amount=60, InstapyFollowed=(True, "nonfollowers"), style="FIFO", unfollow_after=90 * 60 * 60,
    #                        sleep_delay=501)



    # маникюр
    # гельлак
    # ногти
    # nailart
    # дизайнногтей
    # manicure
    # nail
    # ногтиминск
    # маникюрминск
    # minsk
    # гельлакминск
    # naildesign
    # минск
    # аппаратныйманикюр
    # комбиманикюр
    # красивыеногти
    # nailsminsk
    # наращиваниеногтей
    # комбинированныйманикюр
    # belarus
    # beauty
    # instanails
    # долговременноепокрытие
    # педикюр
    # шеллак
    # shellac
    # покрытиегельлаком
    # nailsart
    # наращивание


# import json
#
# f = open('fre.json')
# data = json.load(f)
#
# for i in data:
#     print('https://www.instagram.com/'+ i)
