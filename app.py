from model import Post, Product, User

# User.create(
#     username='amir_agha',
#     password='123456'
# )

# Post.create(
#     title='Second post',
#     text='This post is not a very first post.',
#     date='today',
#     author='me',
# )

User.find(username='abbas_agha').update(password='8569')

for i in User.objects:
    print(i)
