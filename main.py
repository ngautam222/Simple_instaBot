from instapy import InstaPy

session = InstaPy(username="YOUR Account", password="your password")
session.login()
session.like_by_tags(['travel', 'bitcoin', 'cricket', 'foodporn','foodlover', 'sports', 'fashion'], amount=60)
session.set_do_follow(True, percentage=35)
session.set_do_comment(True, percentage=50)
session.set_comments(['nice post', 'wow', 'pretty cool dude'])
#hello brotha
session.end()
