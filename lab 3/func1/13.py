{"payload":{"allShortcutsEnabled":true,"fileTree":{"lab3/func1":{"items":[{"name":"1.py","path":"lab3/func1/1.py","contentType":"file"},{"name":"10.py","path":"lab3/func1/10.py","contentType":"file"},{"name":"11.py","path":"lab3/func1/11.py","contentType":"file"},{"name":"12.py","path":"lab3/func1/12.py","contentType":"file"},{"name":"13.py","path":"lab3/func1/13.py","contentType":"file"},{"name":"2.py","path":"lab3/func1/2.py","contentType":"file"},{"name":"3.py","path":"lab3/func1/3.py","contentType":"file"},{"name":"4.py","path":"lab3/func1/4.py","contentType":"file"},{"name":"5.py","path":"lab3/func1/5.py","contentType":"file"},{"name":"6.py","path":"lab3/func1/6.py","contentType":"file"},{"name":"7.py","path":"lab3/func1/7.py","contentType":"file"},{"name":"8.py","path":"lab3/func1/8.py","contentType":"file"},{"name":"9.py","path":"lab3/func1/9.py","contentType":"file"}],"totalCount":13},"lab3":{"items":[{"name":"classes","path":"lab3/classes","contentType":"directory"},{"name":"func1","path":"lab3/func1","contentType":"directory"},{"name":"func2","path":"lab3/func2","contentType":"directory"},{"name":"1.py","path":"lab3/1.py","contentType":"file"},{"name":"functions1.py","path":"lab3/functions1.py","contentType":"file"},{"name":"functions2.py","path":"lab3/functions2.py","contentType":"file"},{"name":"init.py","path":"lab3/init.py","contentType":"file"}],"totalCount":7},"":{"items":[{"name":"lab1","path":"lab1","contentType":"directory"},{"name":"lab2","path":"lab2","contentType":"directory"},{"name":"lab3","path":"lab3","contentType":"directory"},{"name":"lab4","path":"lab4","contentType":"directory"},{"name":"lab5","path":"lab5","contentType":"directory"},{"name":"lab6","path":"lab6","contentType":"directory"},{"name":"README.md","path":"README.md","contentType":"file"}],"totalCount":7}},"fileTreeProcessingTime":8.859614,"foldersToFetch":[],"repo":{"id":611859061,"defaultBranch":"main","name":"pp2","ownerLogin":"progermyn","currentUserCanPush":true,"isFork":true,"isEmpty":false,"createdAt":"2023-03-09T23:31:13.000+06:00","ownerAvatar":"https://avatars.githubusercontent.com/u/123311974?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":false,"refInfo":{"name":"main","listCacheKey":"v0:1678453653.168261","canEdit":true,"refType":"branch","currentOid":"7b576658d65fbf610aa4f70d69a2e87c56a9e87f"},"path":"lab3/func1/13.py","currentUser":{"id":123311974,"login":"progermyn","userEmail":"y_sailaubek@kbtu.kz"},"blob":{"rawLines":["from random import randrange","# -------------------------------------","#13 task","def guess_the_number():","    gue=0","    name=str(input(\"Hello! What is your name?\\n\"))","","    print(\"Well\",name, ',',\"I am thinking of a number between 1 and 20.\")","","    number=randrange(1,21)","","    while True:","        print(\"Take a guess\")","        guess=int(input())","        if number==guess:","            print(\"Good job, KBTU! You guessed my number\",gue, \"in guesses!\")","            break","        elif guess<number:","            gue+=1","            print(\"Your guess is too low.\")","        else:","            gue+=1","            print(\"Your guess is too high.\")","","# print(guess_the_number())"],"stylingDirectives":[[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":11,"cssClass":"pl-s1"},{"start":12,"end":18,"cssClass":"pl-k"},{"start":19,"end":28,"cssClass":"pl-s1"}],[{"start":0,"end":39,"cssClass":"pl-c"}],[{"start":0,"end":8,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":20,"cssClass":"pl-en"}],[{"start":4,"end":7,"cssClass":"pl-s1"},{"start":7,"end":8,"cssClass":"pl-c1"},{"start":8,"end":9,"cssClass":"pl-c1"}],[{"start":4,"end":8,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":9,"end":12,"cssClass":"pl-en"},{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":48,"cssClass":"pl-s"},{"start":45,"end":47,"cssClass":"pl-cce"}],[],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":16,"cssClass":"pl-s"},{"start":17,"end":21,"cssClass":"pl-s1"},{"start":23,"end":26,"cssClass":"pl-s"},{"start":27,"end":72,"cssClass":"pl-s"}],[],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":11,"end":20,"cssClass":"pl-en"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":25,"cssClass":"pl-c1"}],[],[{"start":4,"end":9,"cssClass":"pl-k"},{"start":10,"end":14,"cssClass":"pl-c1"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":28,"cssClass":"pl-s"}],[{"start":8,"end":13,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":14,"end":17,"cssClass":"pl-en"},{"start":18,"end":23,"cssClass":"pl-en"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":17,"cssClass":"pl-s1"},{"start":17,"end":19,"cssClass":"pl-c1"},{"start":19,"end":24,"cssClass":"pl-s1"}],[{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":57,"cssClass":"pl-s"},{"start":58,"end":61,"cssClass":"pl-s1"},{"start":63,"end":76,"cssClass":"pl-s"}],[{"start":12,"end":17,"cssClass":"pl-k"}],[{"start":8,"end":12,"cssClass":"pl-k"},{"start":13,"end":18,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":19,"end":25,"cssClass":"pl-s1"}],[{"start":12,"end":15,"cssClass":"pl-s1"},{"start":15,"end":17,"cssClass":"pl-c1"},{"start":17,"end":18,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":42,"cssClass":"pl-s"}],[{"start":8,"end":12,"cssClass":"pl-k"}],[{"start":12,"end":15,"cssClass":"pl-s1"},{"start":15,"end":17,"cssClass":"pl-c1"},{"start":17,"end":18,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":43,"cssClass":"pl-s"}],[],[{"start":0,"end":27,"cssClass":"pl-c"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":null,"configFilePath":null,"networkDependabotPath":"/progermyn/pp2/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false,"repoAlertsPath":"/progermyn/pp2/security/dependabot","repoSecurityAndAnalysisPath":"/progermyn/pp2/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":true},"displayName":"13.py","displayUrl":"https://github.com/progermyn/pp2/blob/main/lab3/func1/13.py?raw=true","headerInfo":{"blobSize":"659 Bytes","deleteInfo":{"deleteTooltip":"Delete this file"},"editInfo":{"editTooltip":"Edit this file"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"d454156","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fprogermyn%2Fpp2%2Fblob%2Fmain%2Flab3%2Ffunc1%2F13.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"25","truncatedSloc":"21"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":true,"newDiscussionPath":"/progermyn/pp2/discussions/new","newIssuePath":"/progermyn/pp2/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/progermyn/pp2/blob/main/lab3/func1/13.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/progermyn/pp2/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/progermyn/pp2/raw/main/lab3/func1/13.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"progermyn","repoName":"pp2","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":null,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"guess_the_number","kind":"function","ident_start":82,"ident_end":98,"extent_start":78,"extent_end":629,"fully_qualified_name":"guess_the_number","ident_utf16":{"start":{"line_number":3,"utf16_col":4},"end":{"line_number":3,"utf16_col":20}},"extent_utf16":{"start":{"line_number":3,"utf16_col":0},"end":{"line_number":22,"utf16_col":44}}}]}},"copilotInfo":{"documentationUrl":"https://docs.github.com/copilot/overview-of-github-copilot/about-github-copilot-for-individuals","notices":{"codeViewPopover":{"dismissed":false,"dismissPath":"/settings/dismiss-notice/code_view_copilot_popover"}},"userAccess":{"accessAllowed":false,"hasSubscriptionEnded":false,"orgHasCFBAccess":false,"userHasCFIAccess":false,"userHasOrgs":false,"userIsOrgAdmin":false,"userIsOrgMember":false,"business":null,"featureRequestInfo":null}},"copilotAccessAllowed":false,"csrf_tokens":{"/progermyn/pp2/branches":{"post":"HBiN46ZP28D618p31ALJ2LhGt9ZDaj4wiEonWP8209yucB8-RakI0WZPcZWxuk70cIl7K7HGq-xvdIPtpE3_Yg"},"/repos/preferences":{"post":"NomruGtsmjnbf5nh87OsG8HTmGvJADojpCCOds7bUs0nV4ik6EDklSZP_RmJD5oRlxfINMVvNwo-SgfcwSRtQg"}}},"title":"pp2/lab3/func1/13.py at main · progermyn/pp2"}