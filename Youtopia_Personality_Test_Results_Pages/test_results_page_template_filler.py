import pandas as pd

#load df from csv
csv_filepath = "Youtopia_Personality_Test_Results_Pages/Youtopia Test Results Page Content - Sheet1.csv"

df = pd.read_csv(csv_filepath)

with open("Youtopia_Personality_Test_Results_Pages/test_results_rendered.txt", "w") as file:
    for index, row in df.iterrows():
        text=  """<div class="top-row" style="background-color: {background_color}; ">
<h2>You are {tribe_indefinite_article} {tribe} ({mbti})!</h2>
[mks_col]
[mks_one_third]
<img src="{animal_image_src}">
[/mks_one_third]
[mks_two_thirds]

{short_description}
<div><a class="bob" href="https://www.projectyoutopia.com/the-power-of-personality">Learn more</a></div>
[/mks_two_thirds]
[/mks_col]

</div>
<div class="bottom-row">[mks_col]
[mks_one_third]
<div id="mc_embed_signup">
<div id="book_ad" style="text-align: center;">
<div>Want to learn more about your type?
<strong>Buy <a href="https://www.projectyoutopia.com/the-power-of-personality"><i>The Power of Personality</i></a> by Eric Gee!</strong></div>
<div><a href="https://www.projectyoutopia.com/the-power-of-personality">
<img style="max-height: 300px" src="https://youtopiaproject.com/wp-content/uploads/2023/11/ThePowerOfPersonality-scaled.jpg" alt="Power of Personality Book Cover" /></a></div>
<form id="mc-embedded-subscribe-form" class="validate" action="https://gmail.us8.list-manage.com/subscribe/post?u=92573f0faf58e75dac24eba0b&amp;id=28572bed5d" method="post" name="mc-embedded-subscribe-form" novalidate="" target="_blank">
<div>From the creator of Youtopia Project</div>
</div>
<div id="mc_embed_signup_scroll"><!-- ______________________________ -->
<h5>Stay updated on Youtopia</h5>
<div class="mc-field-group"><input id="mce-EMAIL" class="required email" name="EMAIL" type="email" value="" placeholder="Email Address"></div>
<input name="group[22277]" type="hidden" value="{tribe_value}"><!--ESTJ=1,ISTJ=2,ESFJ=4,ISFJ=8,ESTP=16,ISTP=32,ESFP=64,ISFP=128,ENFJ=256,INFJ=512,ENFP=1024,INFP=2048,ENTJ=4096,INTJ=8192,ENTP=16384,INTP=32768-->
<div id="mce-responses" class="clear">
<div id="mce-error-response" class="response" style="display: none;"></div>
<div id="mce-success-response" class="response" style="display: none;"></div>
</div>
<div style="position: absolute; left: -5000px;" aria-hidden="true"><input tabindex="-1" name="b_92573f0faf58e75dac24eba0b_28572bed5d" type="text" value=""></div>
<div class="clear"><input id="mc-embedded-subscribe" class="bob" name="subscribe" type="submit" value="Save my result and subscribe"></div>
</div>
</form></div>
<script type="text/javascript" src="//s3.amazonaws.com/downloads.mailchimp.com/js/mc-validate.js"></script><script type="text/javascript">(function($) {{window.fnames = new Array(); window.ftypes = new Array();fnames[0]='EMAIL';ftypes[0]='email';fnames[1]='FNAME';ftypes[1]='text';fnames[2]='LNAME';ftypes[2]='text';fnames[3]='ADDRESS';ftypes[3]='address';fnames[4]='PHONE';ftypes[4]='phone';}}(jQuery));var $mcj = jQuery.noConflict(true);</script><!--End mc_embed_signup-->
[/mks_one_third]
[mks_two_thirds]
<h5>Your Deviant Role</h5>
<div>Take the purest ideal of your type, and twist it until it’s nothing more than a gnarled monstrosity of human pathos. That is your <strong>Deviant Role</strong>.</div>
<div><a href="https://youtopiaproject.com/what-is-a-deviant-role">Learn more about Deviant Roles</a></div>
<a href="{deviant_role_img_href}" target="_blank" rel="noopener noreferrer"><img src="{deviant_role_img_src}" alt=""></a>
[/mks_two_thirds]
[/mks_col]

</div>
 	<link rel="stylesheet" href="/test-results.css">
    \n""".format(
        tribe = row['tribe'],
        mbti = row['mbti'],
        tribe_indefinite_article = row['tribe_indefinite_article'],
        background_color = row['background_color'],
        animal_image_src = row['animal_image_src'],
        short_description = row['short_description'],
        deviant_role_img_href = row['deviant_role_img_href'],
        deviant_role_img_src = row['deviant_role_img_src'],
        tribe_value = row['tribe_value']
    )
        file.write(text)