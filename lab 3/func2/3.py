{"payload":{"allShortcutsEnabled":true,"fileTree":{"lab3/func2":{"items":[{"name":"1.py","path":"lab3/func2/1.py","contentType":"file"},{"name":"2.py","path":"lab3/func2/2.py","contentType":"file"},{"name":"3.py","path":"lab3/func2/3.py","contentType":"file"},{"name":"4.py","path":"lab3/func2/4.py","contentType":"file"},{"name":"5.py","path":"lab3/func2/5.py","contentType":"file"}],"totalCount":5},"lab3":{"items":[{"name":"classes","path":"lab3/classes","contentType":"directory"},{"name":"func1","path":"lab3/func1","contentType":"directory"},{"name":"func2","path":"lab3/func2","contentType":"directory"},{"name":"1.py","path":"lab3/1.py","contentType":"file"},{"name":"functions1.py","path":"lab3/functions1.py","contentType":"file"},{"name":"functions2.py","path":"lab3/functions2.py","contentType":"file"},{"name":"init.py","path":"lab3/init.py","contentType":"file"}],"totalCount":7},"":{"items":[{"name":"lab1","path":"lab1","contentType":"directory"},{"name":"lab2","path":"lab2","contentType":"directory"},{"name":"lab3","path":"lab3","contentType":"directory"},{"name":"lab4","path":"lab4","contentType":"directory"},{"name":"lab5","path":"lab5","contentType":"directory"},{"name":"lab6","path":"lab6","contentType":"directory"},{"name":"README.md","path":"README.md","contentType":"file"}],"totalCount":7}},"fileTreeProcessingTime":4.1996389999999995,"foldersToFetch":[],"repo":{"id":611859061,"defaultBranch":"main","name":"pp2","ownerLogin":"progermyn","currentUserCanPush":true,"isFork":true,"isEmpty":false,"createdAt":"2023-03-09T23:31:13.000+06:00","ownerAvatar":"https://avatars.githubusercontent.com/u/123311974?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":false,"refInfo":{"name":"main","listCacheKey":"v0:1678453653.168261","canEdit":true,"refType":"branch","currentOid":"7b576658d65fbf610aa4f70d69a2e87c56a9e87f"},"path":"lab3/func2/3.py","currentUser":{"id":123311974,"login":"progermyn","userEmail":"y_sailaubek@kbtu.kz"},"blob":{"rawLines":["movies = [","{","\"name\": \"Usual Suspects\", ","\"imdb\": 7.0,","\"category\": \"Thriller\"","},","{","\"name\": \"Hitman\",","\"imdb\": 6.3,","\"category\": \"Action\"","},","{","\"name\": \"Dark Knight\",","\"imdb\": 9.0,","\"category\": \"Adventure\"","},","{","\"name\": \"The Help\",","\"imdb\": 8.0,","\"category\": \"Drama\"","},","{","\"name\": \"The Choice\",","\"imdb\": 6.2,","\"category\": \"Romance\"","},","{","\"name\": \"Colonia\",","\"imdb\": 7.4,","\"category\": \"Romance\"","},","{","\"name\": \"Love\",","\"imdb\": 6.0,","\"category\": \"Romance\"","},","{","\"name\": \"Bride Wars\",","\"imdb\": 5.4,","\"category\": \"Romance\"","},","{","\"name\": \"AlphaJet\",","\"imdb\": 3.2,","\"category\": \"War\"","},","{","\"name\": \"Ringing Crime\",","\"imdb\": 4.0,","\"category\": \"Crime\"","},","{","\"name\": \"Joking muck\",","\"imdb\": 7.2,","\"category\": \"Comedy\"","},","{","\"name\": \"What is the name\",","\"imdb\": 9.2,","\"category\": \"Suspense\"","},","{","\"name\": \"Detective\",","\"imdb\": 7.0,","\"category\": \"Suspense\"","},","{","\"name\": \"Exam\",","\"imdb\": 4.2,","\"category\": \"Thriller\"","},","{","\"name\": \"We Two\",","\"imdb\": 7.2,","\"category\": \"Romance\"","}","]","# 3 task","def category_movies(name):","    b=[]","    for i in movies:","        if i['category']==name:","            b.append(i['name'])","    return b","","# print(category_movies('Romance'))"],"stylingDirectives":[[{"start":0,"end":6,"cssClass":"pl-s1"},{"start":7,"end":8,"cssClass":"pl-c1"}],[],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":24,"cssClass":"pl-s"}],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":11,"cssClass":"pl-c1"}],[{"start":0,"end":10,"cssClass":"pl-s"},{"start":12,"end":22,"cssClass":"pl-s"}],[],[],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":16,"cssClass":"pl-s"}],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":11,"cssClass":"pl-c1"}],[{"start":0,"end":10,"cssClass":"pl-s"},{"start":12,"end":20,"cssClass":"pl-s"}],[],[],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":21,"cssClass":"pl-s"}],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":11,"cssClass":"pl-c1"}],[{"start":0,"end":10,"cssClass":"pl-s"},{"start":12,"end":23,"cssClass":"pl-s"}],[],[],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":18,"cssClass":"pl-s"}],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":11,"cssClass":"pl-c1"}],[{"start":0,"end":10,"cssClass":"pl-s"},{"start":12,"end":19,"cssClass":"pl-s"}],[],[],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":20,"cssClass":"pl-s"}],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":11,"cssClass":"pl-c1"}],[{"start":0,"end":10,"cssClass":"pl-s"},{"start":12,"end":21,"cssClass":"pl-s"}],[],[],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":17,"cssClass":"pl-s"}],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":11,"cssClass":"pl-c1"}],[{"start":0,"end":10,"cssClass":"pl-s"},{"start":12,"end":21,"cssClass":"pl-s"}],[],[],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":14,"cssClass":"pl-s"}],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":11,"cssClass":"pl-c1"}],[{"start":0,"end":10,"cssClass":"pl-s"},{"start":12,"end":21,"cssClass":"pl-s"}],[],[],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":20,"cssClass":"pl-s"}],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":11,"cssClass":"pl-c1"}],[{"start":0,"end":10,"cssClass":"pl-s"},{"start":12,"end":21,"cssClass":"pl-s"}],[],[],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":18,"cssClass":"pl-s"}],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":11,"cssClass":"pl-c1"}],[{"start":0,"end":10,"cssClass":"pl-s"},{"start":12,"end":17,"cssClass":"pl-s"}],[],[],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":23,"cssClass":"pl-s"}],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":11,"cssClass":"pl-c1"}],[{"start":0,"end":10,"cssClass":"pl-s"},{"start":12,"end":19,"cssClass":"pl-s"}],[],[],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":21,"cssClass":"pl-s"}],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":11,"cssClass":"pl-c1"}],[{"start":0,"end":10,"cssClass":"pl-s"},{"start":12,"end":20,"cssClass":"pl-s"}],[],[],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":26,"cssClass":"pl-s"}],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":11,"cssClass":"pl-c1"}],[{"start":0,"end":10,"cssClass":"pl-s"},{"start":12,"end":22,"cssClass":"pl-s"}],[],[],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":19,"cssClass":"pl-s"}],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":11,"cssClass":"pl-c1"}],[{"start":0,"end":10,"cssClass":"pl-s"},{"start":12,"end":22,"cssClass":"pl-s"}],[],[],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":14,"cssClass":"pl-s"}],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":11,"cssClass":"pl-c1"}],[{"start":0,"end":10,"cssClass":"pl-s"},{"start":12,"end":22,"cssClass":"pl-s"}],[],[],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":16,"cssClass":"pl-s"}],[{"start":0,"end":6,"cssClass":"pl-s"},{"start":8,"end":11,"cssClass":"pl-c1"}],[{"start":0,"end":10,"cssClass":"pl-s"},{"start":12,"end":21,"cssClass":"pl-s"}],[],[],[{"start":0,"end":8,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":19,"cssClass":"pl-en"},{"start":20,"end":24,"cssClass":"pl-s1"}],[{"start":4,"end":5,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":12,"cssClass":"pl-c1"},{"start":13,"end":19,"cssClass":"pl-s1"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":12,"cssClass":"pl-s1"},{"start":13,"end":23,"cssClass":"pl-s"},{"start":24,"end":26,"cssClass":"pl-c1"},{"start":26,"end":30,"cssClass":"pl-s1"}],[{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":20,"cssClass":"pl-en"},{"start":21,"end":22,"cssClass":"pl-s1"},{"start":23,"end":29,"cssClass":"pl-s"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":12,"cssClass":"pl-s1"}],[],[{"start":0,"end":35,"cssClass":"pl-c"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":null,"configFilePath":null,"networkDependabotPath":"/progermyn/pp2/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false,"repoAlertsPath":"/progermyn/pp2/security/dependabot","repoSecurityAndAnalysisPath":"/progermyn/pp2/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":true},"displayName":"3.py","displayUrl":"https://github.com/progermyn/pp2/blob/main/lab3/func2/3.py?raw=true","headerInfo":{"blobSize":"1.08 KB","deleteInfo":{"deleteTooltip":"Delete this file"},"editInfo":{"editTooltip":"Edit this file"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"cba511f","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fprogermyn%2Fpp2%2Fblob%2Fmain%2Flab3%2Ffunc2%2F3.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"86","truncatedSloc":"85"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":true,"newDiscussionPath":"/progermyn/pp2/discussions/new","newIssuePath":"/progermyn/pp2/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/progermyn/pp2/blob/main/lab3/func2/3.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/progermyn/pp2/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/progermyn/pp2/raw/main/lab3/func2/3.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"progermyn","repoName":"pp2","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":null,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"movies","kind":"constant","ident_start":0,"ident_end":6,"extent_start":0,"extent_end":925,"fully_qualified_name":"movies","ident_utf16":{"start":{"line_number":0,"utf16_col":0},"end":{"line_number":0,"utf16_col":6}},"extent_utf16":{"start":{"line_number":0,"utf16_col":0},"end":{"line_number":76,"utf16_col":1}}},{"name":"category_movies","kind":"function","ident_start":939,"ident_end":954,"extent_start":935,"extent_end":1068,"fully_qualified_name":"category_movies","ident_utf16":{"start":{"line_number":78,"utf16_col":4},"end":{"line_number":78,"utf16_col":19}},"extent_utf16":{"start":{"line_number":78,"utf16_col":0},"end":{"line_number":83,"utf16_col":12}}}]}},"copilotInfo":{"documentationUrl":"https://docs.github.com/copilot/overview-of-github-copilot/about-github-copilot-for-individuals","notices":{"codeViewPopover":{"dismissed":false,"dismissPath":"/settings/dismiss-notice/code_view_copilot_popover"}},"userAccess":{"accessAllowed":false,"hasSubscriptionEnded":false,"orgHasCFBAccess":false,"userHasCFIAccess":false,"userHasOrgs":false,"userIsOrgAdmin":false,"userIsOrgMember":false,"business":null,"featureRequestInfo":null}},"copilotAccessAllowed":false,"csrf_tokens":{"/progermyn/pp2/branches":{"post":"76cWUFi1YJJPi4zPW0kV2JHuo4EREg7rXVAjdcXPdyhdz4SNu1Ozg9MTNy0-8ZL0WSFvfOO-mze6bofAnrRblg"},"/repos/preferences":{"post":"4l6PhCtgp2VNNC8dZ-D71L_V04qSMUdbhnlYbGbYeibzgKyYqEzZybAES-UdXM3e6RGD1Z5eSnIcE9HGaSdFqQ"}}},"title":"pp2/lab3/func2/3.py at main · progermyn/pp2"}