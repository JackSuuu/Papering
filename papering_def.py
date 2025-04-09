import webbrowser

# https://papers.gceguide.com/A%20Levels/Mathematics%20-%20Further%20(9231)/2022/9231_s22_qp_43.pdf
# https://papers.gceguide.com/A%20Levels/Accounting%20(9706)/2022/9706_s22_qp_33.pdf


def openUrl(subject, year, season, paper):

    # build index for each subject
    if subject == "Mathematics":
        subject = 'mathematics-(9709)'
    elif subject == "Further_Math":
        subject = 'Mathematics%20-%20Further%20(9231)'
    elif subject == "Computer Science(new)":
        subject = 'Computer%20Science%20(for%20first%20examination%20in%202021)%20(9618)'
    elif subject == "Physics":
        subject = 'Physics%20(9702)'
    elif subject == "Sociology":
        subject = "Sociology%20(9699)"
    elif subject == "Psychology":
        subject = "Psychology%20(9990)"
    elif subject == "Economics":
        subject = "Economics%20(9708)"
    elif subject == "Business":
        subject = "Business%20Studies%20%20(9707)"
    elif subject == "Accounting":
        subject = "Accounting%20(9706)"
    elif subject == "Biology":
        subject = "Biology%20(9700)"
    elif subject == "Geography":
        subject = "Geography%20(9696)"
    elif subject == "History(new)":
        subject = "History%20(9489)"
    elif subject == "History(old)":
        subject = "History%20(for%20final%20examination%20in%202021)%20(9389)"

    # Check the season
    if season == 'summer':
        season = 's'  # summer
    elif season == 'winter':
        season = 'w'
    elif season == 'march':
        season = 'm'

    # sample link: https://papers.gceguide.cc/a-levels/mathematics-(9709)/2005/9709_s05_qp_1.pdf
    #              https://papers.gceguide.cc/a-levels/mathematics-(9709)/2001/9709_s01_ms_1.pdf
    que_url = f"https://papers.gceguide.cc/a-levels/{subject}/" \
        f"{str(year)}/{subject[-5:-1]}_{season}{str(year[2:])}_qp_{str(paper)[0]}.pdf"

    ans_url = f"https://papers.gceguide.cc/a-levels/{subject}/" \
        f"{str(year)}/{subject[-5:-1]}_{season}{str(year[2:])}_ms_{str(paper)[0]}.pdf"

    webbrowser.open(que_url)
    webbrowser.open(ans_url)



