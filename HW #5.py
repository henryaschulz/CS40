import praw
import random
import time
import datetime
import traceback

count = 0
# this is the login information for our bot
username='CS40_BOTTY'
password='kisskiss123'
client_id='QvtHiu74lFnMRw' 
client_secret='1a3UwWsGAb1jEW9etY91WpOd5pM'
user_agent='CS_40 Botty'

# connect to reddit 
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=username,
    username=username,
    password=password,
    )
support=['Mayor Pete Buttigieg','Michael Bloomberg', 'Mayor Pete', 'Mayor Buttigieg', 'Pete Buttigieg', 'Mike Bloomberg', 'Mayor Bloomberg']
against=['Elizabeth Warren,' 'Bernie Sanders', 'Joe Biden', 'Kamala Harris', 'Julian Castro', 'Andrew Yang', 'Marianne Williamson', 'Amy Klobuchar']
negative=['too liberal', 'a socialist', ' the DC establishment', '2016 all over again', 'a Democrat\'s worst nightmare', 'part of the Liberal Elites']
positive=['a Policy Wonk', 'articulate', 'a city executive', 'youthful', 'politically savvy', 'managerial and political', 'successful', 'an intellectual']
policy=['Medicare for All', 'Medicare for All Who Want It', 'Decriminalize illegal border crossings', 'Repeal AUMF', 'gun control']


pattern1='<support> is <positive> because he has experience as a city mayor. He will win this election.'
pattern2='<against> is <negative> because <policy> will get Trump re-elected. That is not what the American people want.'
pattern3='<policy> is a winning policy because in the general election, <support> will be able to win over disillusioned Trump voters and independents. It is a good platform and will win them the election'
pattern4='<support>  can beat Donald Trump because the candidate has intelligent policies like <policy>. Also, he has both political and business experience.'
pattern5='Mayor Pete\'s <policy> is also a sound electoral strategy because it appeals to a broad base. It will work better that <against>\'s narrow policies.'
pattern6= 'Michael Bloomberg is <positive> because he was a three term mayor in NYC. This gives him the experience to run the country.'

patterns=[pattern1, pattern2, pattern3, pattern4, pattern5, pattern6]


with open ('index.html', 'w') as f:
    content= ('<head>'+
           '<meta name="description" content="This will outline my bot\'s conversations.">'+
           '<title> Homework #5 </title>' +'<h1> Coding Reddit bots</h1>'+
           '<p> My bot is posting is posting on behalf of Pete Buttigege and Mike Bloomberg</p>' +
           '<img src="screenshot reddit.png' 'alt="Bot conversation screenshot.">'+
           '<h3> My favorite discussion: </h3> <a href="https://www.reddit.com/r/csci040/comments/dw53wt/political_discussion_thread/f8sjrrp?utm_source=share&utm_medium=web2x"> Link</a>'+
           '<p> My favorite conversation was my bot\'s exchange with anniecave under the political discussion thread. I enjoyed this exchange because after my comment about Mayor Pete,' +
              'jhaughton commented and defended Warren. I thought this simulated a real conversation on social media in which someone states their political opinion and a stranger comments and defends the original commentor.'
           '<h3> My Score should be: </h3>' +
           '<p> I should get 90 for completing all of the tasks, 5 for upvoting the comments having to do with my candidates'+
           ', 5 for writing over 200 comments, and 10 for posting 20 plagerized comments.' +
           'this totals 110/100points.</p>')
    f.write(content)
    print('Website written')

# FIXME (task 1): the submission variable should be a praw submission object that
# points to the bot political discussion thread at
# https://www.reddit.com/r/csci040/comments/dw53wt/political_discussion_thread/
# HINT: there is a one-line command in the praw quick-start guide
# that accomplishes this task.

# in an infinite loop, we will look for comment in the post that we can reply to
while True:
    try:

        result=random.choice(patterns)
        result=result.replace('<support>', random.choice(support))
        result=result.replace('<against>', random.choice(against))
        result=result.replace('<negative>', random.choice(negative))
        result=result.replace('<positive>', random.choice(positive))
        result=result.replace('<policy>', random.choice(policy))
        text = result + ' This is a bot posting'
        
        subred = list(reddit.subreddit('csci040').hot())
        sub = random.choice(subred)

        taken = list(reddit.subreddit('Pete_Buttigieg').hot())

        t_title = random.choice(taken).title
        t_text = random.choice(taken).selftext
        reddit.subreddit('csci040').submit(title = 'Plagiarized from r/Pete_Buttigieg ' + t_title, selftext = t_text)
        print('Posted New')
        # printing the current time will help make the output messages more informative
        # since things on reddit vary with time
        print(sub)
        print('new iteration at:',datetime.datetime.now())

        # FIXME (task 2): get a list of all of the comments in the submission
        all_comments = []
        all_comments=sub.comments.list()

        for com in all_comments:
            if 'bloomb' in str(com.body).lower() or 'butti' in str(com.body).lower():
                com.upvote()
                print('Upvote')
                
        if len(all_comments) == 0:
            sub.reply(text)
                
        # HINT1: there is a one-line command in the praw quick-start guide
        # that accomplishes this task.
        # HINT2: whenever we work on a program, you need to somehow check that the
        # things your programming is doing are correct.  In this case, one thing
        # we can do is to check the length of the all_comments variable.
        # You should manually ensure that the printed length is the same as the
        # length displayed on reddit.  If it's not, then tçhere are some comments
        # that you are not correctly identifying, and you need to figure out
        # which comments those are and how to include them.
        print('len(all_comments)=',len(all_comments))

        # FIXME (task 3): filter all_comments to remove comments that were generated by your bot
        not_my_comments=[]
        for com in all_comments:
            if username not in str(com.author):
                not_my_comments.append(com)
        # HINT1: completing this task requires only a single for loop and a single if statement.
        # The PRAW quick-start guide has the contents of the for loop/if statement.
        # HINT2: as before, you need to check that your code is working somehow.
        # reddit does not provide any list of comments generated by your bot,
        # but you can easily check this number manually by subtracting the number
        # of comments you know you've posted from the number above.
        print('len(not_my_comments)=',len(not_my_comments))

        # FIXME (task 4): filter the list to also remove comments that you've already replied to
        comments_without_replies=[]
        x = 0
        for com in not_my_comments:
            x = 0
            for rep in com.replies:
                if username in str(rep.author):
                    x = 1
                if x == 0:
                    comments_without_replies.append(com)
        # HINT1: completing this task requires only a single for loop and a single if statement.
        # The PRAW quick-start guide has the contents of the for loop/if statement.
        # HINT2: again, you need to check that this is working
        if len(comments_without_replies) == 0:
            print('Paused cause no posts that I haven\'t replied to')
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 5): randomly select one of the comments that we haven't replied to yet
        # HINT: There is a function in python's random module for doing this.
        # See the documentation at https://docs.python.org/3/library/random.html
        commentrep = random.choice(comments_without_replies)

        # FIXME (task 6): generate some random text for your comment;
        # your message must clearly identify itself as a bot
        # HINT: This is the same as lab 13.
        

        # FIXME (task 7): post a reply to the selected comment
        # HINT: We covered how to do this in class on 12 Nov.
        # See the reddit.py lecture notes or the PRAW quick start guide.
        
        commentrep.reply(text)
        
        # FIXME (task 8): check all submissions in the /r/csci040 subreddit to see if your
        # bot has not created a top-level comment in that submission.  If it has not,
        # then create a top-level comment.
        # HINT1: The PRAW quick-start guide contains all the information you need to know
        # about PRAW to complete this task.
        # HINT2: The code for this task will have to be placed in multiple places throughout
        # this file.
        
        
        print('Sleeping at end. Will comment again.')
        time.sleep(10*60)
        count += 1
        print('count = ',count)
    except Exception:
        traceback.print_exc()
        print('count = ',count)
        print('There was an Error')
        time.sleep(10*60)
