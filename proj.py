from instapy import InstaPy
from instapy.util import smart_run

session = InstaPy(username="+375336105624", password="3201227QWERT").login()

with smart_run(session):
    """ Activity flow """
    # settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    session.set_dont_include(["friend1", "friend2", "friend3"])
    session.set_dont_like(["pizza", "#store"])
    session.unfollow_users(amount=10)
    # actions
    session.like_by_tags(["natgeo"], amount=10)