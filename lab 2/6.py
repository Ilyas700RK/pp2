{"payload":{"allShortcutsEnabled":true,"fileTree":{"tsis2":{"items":[{"name":"1.py","path":"tsis2/1.py","contentType":"file"},{"name":"2.py","path":"tsis2/2.py","contentType":"file"},{"name":"3.py","path":"tsis2/3.py","contentType":"file"},{"name":"4.py","path":"tsis2/4.py","contentType":"file"},{"name":"5.py","path":"tsis2/5.py","contentType":"file"},{"name":"6.py","path":"tsis2/6.py","contentType":"file"},{"name":"7.py","path":"tsis2/7.py","contentType":"file"}],"totalCount":7},"":{"items":[{"name":"Lab 10","path":"Lab 10","contentType":"directory"},{"name":"Lab 11","path":"Lab 11","contentType":"directory"},{"name":"Lab 8","path":"Lab 8","contentType":"directory"},{"name":"Lab 9","path":"Lab 9","contentType":"directory"},{"name":"tsis1","path":"tsis1","contentType":"directory"},{"name":"tsis2","path":"tsis2","contentType":"directory"},{"name":"tsis3","path":"tsis3","contentType":"directory"},{"name":"tsis4","path":"tsis4","contentType":"directory"},{"name":"tsis5_regex","path":"tsis5_regex","contentType":"directory"},{"name":"tsis6-dir-and-files","path":"tsis6-dir-and-files","contentType":"directory"},{"name":"tsis7","path":"tsis7","contentType":"directory"},{"name":"README.md","path":"README.md","contentType":"file"}],"totalCount":12}},"fileTreeProcessingTime":3.6073329999999997,"foldersToFetch":[],"repo":{"id":599534368,"defaultBranch":"main","name":"pp2-22B031111","ownerLogin":"progermyn","currentUserCanPush":true,"isFork":false,"isEmpty":false,"createdAt":"2023-02-09T16:47:39.000+06:00","ownerAvatar":"https://avatars.githubusercontent.com/u/123311974?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":false,"refInfo":{"name":"main","listCacheKey":"v0:1683268182.0","canEdit":true,"refType":"branch","currentOid":"c2a89b732b0c89fe742599d886be1d397446f91b"},"path":"tsis2/6.py","currentUser":{"id":123311974,"login":"progermyn","userEmail":"y_sailaubek@kbtu.kz"},"blob":{"rawLines":["thisset = {\"apple\", \"banana\", \"cherry\"}\r","print(thisset)\r","\r","\r","thisset = {\"apple\", \"banana\", \"cherry\", \"apple\"}\r","\r","print(thisset)\r","\r","\r","thisset = {\"apple\", \"banana\", \"cherry\"}\r","\r","print(len(thisset))\r","\r","\r","set1 = {\"apple\", \"banana\", \"cherry\"}\r","set2 = {1, 5, 7, 9, 3}\r","set3 = {True, False, False}\r","\r","\r","set1 = {\"abc\", 34, True, 40, \"male\"}\r","\r","\r","myset = {\"apple\", \"banana\", \"cherry\"}\r","print(type(myset))\r","\r","\r","thisset = set((\"apple\", \"banana\", \"cherry\")) # note the double round-brackets\r","print(thisset)\r","\r","\r","thisset = {\"apple\", \"banana\", \"cherry\"}\r","\r","for x in thisset:\r","  print(x)\r","  \r","  \r","thisset = {\"apple\", \"banana\", \"cherry\"}\r","\r","print(\"banana\" in thisset)\r","\r","\r","thisset = {\"apple\", \"banana\", \"cherry\"}\r","\r","thisset.add(\"orange\")\r","\r","print(thisset)\r","\r","\r","thisset = {\"apple\", \"banana\", \"cherry\"}\r","tropical = {\"pineapple\", \"mango\", \"papaya\"}\r","\r","thisset.update(tropical)\r","\r","print(thisset)\r","\r","\r","thisset = {\"apple\", \"banana\", \"cherry\"}\r","mylist = [\"kiwi\", \"orange\"]\r","\r","thisset.update(mylist)\r","\r","print(thisset)\r","\r","\r","thisset = {\"apple\", \"banana\", \"cherry\"}\r","\r","thisset.remove(\"banana\")\r","\r","print(thisset)\r","\r","\r","thisset = {\"apple\", \"banana\", \"cherry\"}\r","\r","thisset.discard(\"banana\")\r","\r","print(thisset)\r","\r","\r","thisset = {\"apple\", \"banana\", \"cherry\"}\r","\r","x = thisset.pop()\r","\r","print(x)\r","\r","print(thisset)\r","\r","\r","thisset = {\"apple\", \"banana\", \"cherry\"}\r","\r","thisset.clear()\r","\r","print(thisset)\r","\r","\r","thisset = {\"apple\", \"banana\", \"cherry\"}\r","\r","del thisset\r","\r","print(thisset)\r","\r","\r","thisset = {\"apple\", \"banana\", \"cherry\"}\r","\r","for x in thisset:\r","  print(x)\r","  \r","  \r","set1 = {\"a\", \"b\" , \"c\"}\r","set2 = {1, 2, 3}\r","\r","set3 = set1.union(set2)\r","print(set3)\r","\r","\r","set1 = {\"a\", \"b\" , \"c\"}\r","set2 = {1, 2, 3}\r","\r","set1.update(set2)\r","print(set1)\r","\r","\r","x = {\"apple\", \"banana\", \"cherry\"}\r","y = {\"google\", \"microsoft\", \"apple\"}\r","\r","x.intersection_update(y)\r","\r","print(x)\r","\r","\r","x = {\"apple\", \"banana\", \"cherry\"}\r","y = {\"google\", \"microsoft\", \"apple\"}\r","\r","z = x.intersection(y)\r","\r","print(z)\r","\r","\r","x = {\"apple\", \"banana\", \"cherry\"}\r","y = {\"google\", \"microsoft\", \"apple\"}\r","\r","x.symmetric_difference_update(y)\r","\r","print(x)\r","\r","\r","x = {\"apple\", \"banana\", \"cherry\"}\r","y = {\"google\", \"microsoft\", \"apple\"}\r","\r","z = x.symmetric_difference(y)\r","\r","print(z)\r","\r","\r"],"stylingDirectives":[[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":11,"end":18,"cssClass":"pl-s"},{"start":20,"end":28,"cssClass":"pl-s"},{"start":30,"end":38,"cssClass":"pl-s"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":13,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":11,"end":18,"cssClass":"pl-s"},{"start":20,"end":28,"cssClass":"pl-s"},{"start":30,"end":38,"cssClass":"pl-s"},{"start":40,"end":47,"cssClass":"pl-s"}],[],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":13,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":11,"end":18,"cssClass":"pl-s"},{"start":20,"end":28,"cssClass":"pl-s"},{"start":30,"end":38,"cssClass":"pl-s"}],[],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":9,"cssClass":"pl-en"},{"start":10,"end":17,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":8,"end":15,"cssClass":"pl-s"},{"start":17,"end":25,"cssClass":"pl-s"},{"start":27,"end":35,"cssClass":"pl-s"}],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":20,"end":21,"cssClass":"pl-c1"}],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":8,"end":12,"cssClass":"pl-c1"},{"start":14,"end":19,"cssClass":"pl-c1"},{"start":21,"end":26,"cssClass":"pl-c1"}],[],[],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":8,"end":13,"cssClass":"pl-s"},{"start":15,"end":17,"cssClass":"pl-c1"},{"start":19,"end":23,"cssClass":"pl-c1"},{"start":25,"end":27,"cssClass":"pl-c1"},{"start":29,"end":35,"cssClass":"pl-s"}],[],[],[{"start":0,"end":5,"cssClass":"pl-s1"},{"start":6,"end":7,"cssClass":"pl-c1"},{"start":9,"end":16,"cssClass":"pl-s"},{"start":18,"end":26,"cssClass":"pl-s"},{"start":28,"end":36,"cssClass":"pl-s"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":10,"cssClass":"pl-en"},{"start":11,"end":16,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":10,"end":13,"cssClass":"pl-en"},{"start":15,"end":22,"cssClass":"pl-s"},{"start":24,"end":32,"cssClass":"pl-s"},{"start":34,"end":42,"cssClass":"pl-s"},{"start":45,"end":78,"cssClass":"pl-c"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":13,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":11,"end":18,"cssClass":"pl-s"},{"start":20,"end":28,"cssClass":"pl-s"},{"start":30,"end":38,"cssClass":"pl-s"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":5,"cssClass":"pl-s1"},{"start":6,"end":8,"cssClass":"pl-c1"},{"start":9,"end":16,"cssClass":"pl-s1"}],[{"start":2,"end":7,"cssClass":"pl-en"},{"start":8,"end":9,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":11,"end":18,"cssClass":"pl-s"},{"start":20,"end":28,"cssClass":"pl-s"},{"start":30,"end":38,"cssClass":"pl-s"}],[],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":14,"cssClass":"pl-s"},{"start":15,"end":17,"cssClass":"pl-c1"},{"start":18,"end":25,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":11,"end":18,"cssClass":"pl-s"},{"start":20,"end":28,"cssClass":"pl-s"},{"start":30,"end":38,"cssClass":"pl-s"}],[],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":11,"cssClass":"pl-en"},{"start":12,"end":20,"cssClass":"pl-s"}],[],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":13,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":11,"end":18,"cssClass":"pl-s"},{"start":20,"end":28,"cssClass":"pl-s"},{"start":30,"end":38,"cssClass":"pl-s"}],[{"start":0,"end":8,"cssClass":"pl-s1"},{"start":9,"end":10,"cssClass":"pl-c1"},{"start":12,"end":23,"cssClass":"pl-s"},{"start":25,"end":32,"cssClass":"pl-s"},{"start":34,"end":42,"cssClass":"pl-s"}],[],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":14,"cssClass":"pl-en"},{"start":15,"end":23,"cssClass":"pl-s1"}],[],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":13,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":11,"end":18,"cssClass":"pl-s"},{"start":20,"end":28,"cssClass":"pl-s"},{"start":30,"end":38,"cssClass":"pl-s"}],[{"start":0,"end":6,"cssClass":"pl-s1"},{"start":7,"end":8,"cssClass":"pl-c1"},{"start":10,"end":16,"cssClass":"pl-s"},{"start":18,"end":26,"cssClass":"pl-s"}],[],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":14,"cssClass":"pl-en"},{"start":15,"end":21,"cssClass":"pl-s1"}],[],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":13,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":11,"end":18,"cssClass":"pl-s"},{"start":20,"end":28,"cssClass":"pl-s"},{"start":30,"end":38,"cssClass":"pl-s"}],[],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":14,"cssClass":"pl-en"},{"start":15,"end":23,"cssClass":"pl-s"}],[],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":13,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":11,"end":18,"cssClass":"pl-s"},{"start":20,"end":28,"cssClass":"pl-s"},{"start":30,"end":38,"cssClass":"pl-s"}],[],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":15,"cssClass":"pl-en"},{"start":16,"end":24,"cssClass":"pl-s"}],[],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":13,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":11,"end":18,"cssClass":"pl-s"},{"start":20,"end":28,"cssClass":"pl-s"},{"start":30,"end":38,"cssClass":"pl-s"}],[],[{"start":0,"end":1,"cssClass":"pl-s1"},{"start":2,"end":3,"cssClass":"pl-c1"},{"start":4,"end":11,"cssClass":"pl-s1"},{"start":12,"end":15,"cssClass":"pl-en"}],[],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":7,"cssClass":"pl-s1"}],[],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":13,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":11,"end":18,"cssClass":"pl-s"},{"start":20,"end":28,"cssClass":"pl-s"},{"start":30,"end":38,"cssClass":"pl-s"}],[],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":13,"cssClass":"pl-en"}],[],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":13,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":11,"end":18,"cssClass":"pl-s"},{"start":20,"end":28,"cssClass":"pl-s"},{"start":30,"end":38,"cssClass":"pl-s"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":11,"cssClass":"pl-s1"}],[],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":13,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":11,"end":18,"cssClass":"pl-s"},{"start":20,"end":28,"cssClass":"pl-s"},{"start":30,"end":38,"cssClass":"pl-s"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":5,"cssClass":"pl-s1"},{"start":6,"end":8,"cssClass":"pl-c1"},{"start":9,"end":16,"cssClass":"pl-s1"}],[{"start":2,"end":7,"cssClass":"pl-en"},{"start":8,"end":9,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":8,"end":11,"cssClass":"pl-s"},{"start":13,"end":16,"cssClass":"pl-s"},{"start":19,"end":22,"cssClass":"pl-s"}],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":14,"end":15,"cssClass":"pl-c1"}],[],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":7,"end":11,"cssClass":"pl-s1"},{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":22,"cssClass":"pl-s1"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":10,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":8,"end":11,"cssClass":"pl-s"},{"start":13,"end":16,"cssClass":"pl-s"},{"start":19,"end":22,"cssClass":"pl-s"}],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":14,"end":15,"cssClass":"pl-c1"}],[],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":5,"end":11,"cssClass":"pl-en"},{"start":12,"end":16,"cssClass":"pl-s1"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":10,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":1,"cssClass":"pl-s1"},{"start":2,"end":3,"cssClass":"pl-c1"},{"start":5,"end":12,"cssClass":"pl-s"},{"start":14,"end":22,"cssClass":"pl-s"},{"start":24,"end":32,"cssClass":"pl-s"}],[{"start":0,"end":1,"cssClass":"pl-s1"},{"start":2,"end":3,"cssClass":"pl-c1"},{"start":5,"end":13,"cssClass":"pl-s"},{"start":15,"end":26,"cssClass":"pl-s"},{"start":28,"end":35,"cssClass":"pl-s"}],[],[{"start":0,"end":1,"cssClass":"pl-s1"},{"start":2,"end":21,"cssClass":"pl-en"},{"start":22,"end":23,"cssClass":"pl-s1"}],[],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":7,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":1,"cssClass":"pl-s1"},{"start":2,"end":3,"cssClass":"pl-c1"},{"start":5,"end":12,"cssClass":"pl-s"},{"start":14,"end":22,"cssClass":"pl-s"},{"start":24,"end":32,"cssClass":"pl-s"}],[{"start":0,"end":1,"cssClass":"pl-s1"},{"start":2,"end":3,"cssClass":"pl-c1"},{"start":5,"end":13,"cssClass":"pl-s"},{"start":15,"end":26,"cssClass":"pl-s"},{"start":28,"end":35,"cssClass":"pl-s"}],[],[{"start":0,"end":1,"cssClass":"pl-s1"},{"start":2,"end":3,"cssClass":"pl-c1"},{"start":4,"end":5,"cssClass":"pl-s1"},{"start":6,"end":18,"cssClass":"pl-en"},{"start":19,"end":20,"cssClass":"pl-s1"}],[],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":7,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":1,"cssClass":"pl-s1"},{"start":2,"end":3,"cssClass":"pl-c1"},{"start":5,"end":12,"cssClass":"pl-s"},{"start":14,"end":22,"cssClass":"pl-s"},{"start":24,"end":32,"cssClass":"pl-s"}],[{"start":0,"end":1,"cssClass":"pl-s1"},{"start":2,"end":3,"cssClass":"pl-c1"},{"start":5,"end":13,"cssClass":"pl-s"},{"start":15,"end":26,"cssClass":"pl-s"},{"start":28,"end":35,"cssClass":"pl-s"}],[],[{"start":0,"end":1,"cssClass":"pl-s1"},{"start":2,"end":29,"cssClass":"pl-en"},{"start":30,"end":31,"cssClass":"pl-s1"}],[],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":7,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":1,"cssClass":"pl-s1"},{"start":2,"end":3,"cssClass":"pl-c1"},{"start":5,"end":12,"cssClass":"pl-s"},{"start":14,"end":22,"cssClass":"pl-s"},{"start":24,"end":32,"cssClass":"pl-s"}],[{"start":0,"end":1,"cssClass":"pl-s1"},{"start":2,"end":3,"cssClass":"pl-c1"},{"start":5,"end":13,"cssClass":"pl-s"},{"start":15,"end":26,"cssClass":"pl-s"},{"start":28,"end":35,"cssClass":"pl-s"}],[],[{"start":0,"end":1,"cssClass":"pl-s1"},{"start":2,"end":3,"cssClass":"pl-c1"},{"start":4,"end":5,"cssClass":"pl-s1"},{"start":6,"end":26,"cssClass":"pl-en"},{"start":27,"end":28,"cssClass":"pl-s1"}],[],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":7,"cssClass":"pl-s1"}],[],[]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":null,"configFilePath":null,"networkDependabotPath":"/progermyn/pp2-22B031111/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false,"repoAlertsPath":"/progermyn/pp2-22B031111/security/dependabot","repoSecurityAndAnalysisPath":"/progermyn/pp2-22B031111/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":true},"displayName":"6.py","displayUrl":"https://github.com/progermyn/pp2-22B031111/blob/main/tsis2/6.py?raw=true","headerInfo":{"blobSize":"2.12 KB","deleteInfo":{"deleteTooltip":"Delete this file"},"editInfo":{"editTooltip":"Edit this file"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"e1facfb","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fprogermyn%2Fpp2-22B031111%2Fblob%2Fmain%2Ftsis2%2F6.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"153","truncatedSloc":"73"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":true,"newDiscussionPath":"/progermyn/pp2-22B031111/discussions/new","newIssuePath":"/progermyn/pp2-22B031111/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/progermyn/pp2-22B031111/blob/main/tsis2/6.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/progermyn/pp2-22B031111/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/progermyn/pp2-22B031111/raw/main/tsis2/6.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"progermyn","repoName":"pp2-22B031111","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":null,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"thisset","kind":"constant","ident_start":0,"ident_end":7,"extent_start":0,"extent_end":39,"fully_qualified_name":"thisset","ident_utf16":{"start":{"line_number":0,"utf16_col":0},"end":{"line_number":0,"utf16_col":7}},"extent_utf16":{"start":{"line_number":0,"utf16_col":0},"end":{"line_number":0,"utf16_col":39}}},{"name":"thisset","kind":"constant","ident_start":61,"ident_end":68,"extent_start":61,"extent_end":109,"fully_qualified_name":"thisset","ident_utf16":{"start":{"line_number":4,"utf16_col":0},"end":{"line_number":4,"utf16_col":7}},"extent_utf16":{"start":{"line_number":4,"utf16_col":0},"end":{"line_number":4,"utf16_col":48}}},{"name":"thisset","kind":"constant","ident_start":133,"ident_end":140,"extent_start":133,"extent_end":172,"fully_qualified_name":"thisset","ident_utf16":{"start":{"line_number":9,"utf16_col":0},"end":{"line_number":9,"utf16_col":7}},"extent_utf16":{"start":{"line_number":9,"utf16_col":0},"end":{"line_number":9,"utf16_col":39}}},{"name":"set1","kind":"constant","ident_start":201,"ident_end":205,"extent_start":201,"extent_end":237,"fully_qualified_name":"set1","ident_utf16":{"start":{"line_number":14,"utf16_col":0},"end":{"line_number":14,"utf16_col":4}},"extent_utf16":{"start":{"line_number":14,"utf16_col":0},"end":{"line_number":14,"utf16_col":36}}},{"name":"set2","kind":"constant","ident_start":239,"ident_end":243,"extent_start":239,"extent_end":261,"fully_qualified_name":"set2","ident_utf16":{"start":{"line_number":15,"utf16_col":0},"end":{"line_number":15,"utf16_col":4}},"extent_utf16":{"start":{"line_number":15,"utf16_col":0},"end":{"line_number":15,"utf16_col":22}}},{"name":"set3","kind":"constant","ident_start":263,"ident_end":267,"extent_start":263,"extent_end":290,"fully_qualified_name":"set3","ident_utf16":{"start":{"line_number":16,"utf16_col":0},"end":{"line_number":16,"utf16_col":4}},"extent_utf16":{"start":{"line_number":16,"utf16_col":0},"end":{"line_number":16,"utf16_col":27}}},{"name":"set1","kind":"constant","ident_start":296,"ident_end":300,"extent_start":296,"extent_end":332,"fully_qualified_name":"set1","ident_utf16":{"start":{"line_number":19,"utf16_col":0},"end":{"line_number":19,"utf16_col":4}},"extent_utf16":{"start":{"line_number":19,"utf16_col":0},"end":{"line_number":19,"utf16_col":36}}},{"name":"myset","kind":"constant","ident_start":338,"ident_end":343,"extent_start":338,"extent_end":375,"fully_qualified_name":"myset","ident_utf16":{"start":{"line_number":22,"utf16_col":0},"end":{"line_number":22,"utf16_col":5}},"extent_utf16":{"start":{"line_number":22,"utf16_col":0},"end":{"line_number":22,"utf16_col":37}}},{"name":"thisset","kind":"constant","ident_start":401,"ident_end":408,"extent_start":401,"extent_end":445,"fully_qualified_name":"thisset","ident_utf16":{"start":{"line_number":26,"utf16_col":0},"end":{"line_number":26,"utf16_col":7}},"extent_utf16":{"start":{"line_number":26,"utf16_col":0},"end":{"line_number":26,"utf16_col":44}}},{"name":"thisset","kind":"constant","ident_start":500,"ident_end":507,"extent_start":500,"extent_end":539,"fully_qualified_name":"thisset","ident_utf16":{"start":{"line_number":30,"utf16_col":0},"end":{"line_number":30,"utf16_col":7}},"extent_utf16":{"start":{"line_number":30,"utf16_col":0},"end":{"line_number":30,"utf16_col":39}}},{"name":"thisset","kind":"constant","ident_start":582,"ident_end":589,"extent_start":582,"extent_end":621,"fully_qualified_name":"thisset","ident_utf16":{"start":{"line_number":36,"utf16_col":0},"end":{"line_number":36,"utf16_col":7}},"extent_utf16":{"start":{"line_number":36,"utf16_col":0},"end":{"line_number":36,"utf16_col":39}}},{"name":"thisset","kind":"constant","ident_start":657,"ident_end":664,"extent_start":657,"extent_end":696,"fully_qualified_name":"thisset","ident_utf16":{"start":{"line_number":41,"utf16_col":0},"end":{"line_number":41,"utf16_col":7}},"extent_utf16":{"start":{"line_number":41,"utf16_col":0},"end":{"line_number":41,"utf16_col":39}}},{"name":"thisset","kind":"constant","ident_start":745,"ident_end":752,"extent_start":745,"extent_end":784,"fully_qualified_name":"thisset","ident_utf16":{"start":{"line_number":48,"utf16_col":0},"end":{"line_number":48,"utf16_col":7}},"extent_utf16":{"start":{"line_number":48,"utf16_col":0},"end":{"line_number":48,"utf16_col":39}}},{"name":"tropical","kind":"constant","ident_start":786,"ident_end":794,"extent_start":786,"extent_end":829,"fully_qualified_name":"tropical","ident_utf16":{"start":{"line_number":49,"utf16_col":0},"end":{"line_number":49,"utf16_col":8}},"extent_utf16":{"start":{"line_number":49,"utf16_col":0},"end":{"line_number":49,"utf16_col":43}}},{"name":"thisset","kind":"constant","ident_start":881,"ident_end":888,"extent_start":881,"extent_end":920,"fully_qualified_name":"thisset","ident_utf16":{"start":{"line_number":56,"utf16_col":0},"end":{"line_number":56,"utf16_col":7}},"extent_utf16":{"start":{"line_number":56,"utf16_col":0},"end":{"line_number":56,"utf16_col":39}}},{"name":"mylist","kind":"constant","ident_start":922,"ident_end":928,"extent_start":922,"extent_end":949,"fully_qualified_name":"mylist","ident_utf16":{"start":{"line_number":57,"utf16_col":0},"end":{"line_number":57,"utf16_col":6}},"extent_utf16":{"start":{"line_number":57,"utf16_col":0},"end":{"line_number":57,"utf16_col":27}}},{"name":"thisset","kind":"constant","ident_start":999,"ident_end":1006,"extent_start":999,"extent_end":1038,"fully_qualified_name":"thisset","ident_utf16":{"start":{"line_number":64,"utf16_col":0},"end":{"line_number":64,"utf16_col":7}},"extent_utf16":{"start":{"line_number":64,"utf16_col":0},"end":{"line_number":64,"utf16_col":39}}},{"name":"thisset","kind":"constant","ident_start":1090,"ident_end":1097,"extent_start":1090,"extent_end":1129,"fully_qualified_name":"thisset","ident_utf16":{"start":{"line_number":71,"utf16_col":0},"end":{"line_number":71,"utf16_col":7}},"extent_utf16":{"start":{"line_number":71,"utf16_col":0},"end":{"line_number":71,"utf16_col":39}}},{"name":"thisset","kind":"constant","ident_start":1182,"ident_end":1189,"extent_start":1182,"extent_end":1221,"fully_qualified_name":"thisset","ident_utf16":{"start":{"line_number":78,"utf16_col":0},"end":{"line_number":78,"utf16_col":7}},"extent_utf16":{"start":{"line_number":78,"utf16_col":0},"end":{"line_number":78,"utf16_col":39}}},{"name":"x","kind":"constant","ident_start":1225,"ident_end":1226,"extent_start":1225,"extent_end":1242,"fully_qualified_name":"x","ident_utf16":{"start":{"line_number":80,"utf16_col":0},"end":{"line_number":80,"utf16_col":1}},"extent_utf16":{"start":{"line_number":80,"utf16_col":0},"end":{"line_number":80,"utf16_col":17}}},{"name":"thisset","kind":"constant","ident_start":1278,"ident_end":1285,"extent_start":1278,"extent_end":1317,"fully_qualified_name":"thisset","ident_utf16":{"start":{"line_number":87,"utf16_col":0},"end":{"line_number":87,"utf16_col":7}},"extent_utf16":{"start":{"line_number":87,"utf16_col":0},"end":{"line_number":87,"utf16_col":39}}},{"name":"thisset","kind":"constant","ident_start":1360,"ident_end":1367,"extent_start":1360,"extent_end":1399,"fully_qualified_name":"thisset","ident_utf16":{"start":{"line_number":94,"utf16_col":0},"end":{"line_number":94,"utf16_col":7}},"extent_utf16":{"start":{"line_number":94,"utf16_col":0},"end":{"line_number":94,"utf16_col":39}}},{"name":"thisset","kind":"constant","ident_start":1438,"ident_end":1445,"extent_start":1438,"extent_end":1477,"fully_qualified_name":"thisset","ident_utf16":{"start":{"line_number":101,"utf16_col":0},"end":{"line_number":101,"utf16_col":7}},"extent_utf16":{"start":{"line_number":101,"utf16_col":0},"end":{"line_number":101,"utf16_col":39}}},{"name":"set1","kind":"constant","ident_start":1520,"ident_end":1524,"extent_start":1520,"extent_end":1543,"fully_qualified_name":"set1","ident_utf16":{"start":{"line_number":107,"utf16_col":0},"end":{"line_number":107,"utf16_col":4}},"extent_utf16":{"start":{"line_number":107,"utf16_col":0},"end":{"line_number":107,"utf16_col":23}}},{"name":"set2","kind":"constant","ident_start":1545,"ident_end":1549,"extent_start":1545,"extent_end":1561,"fully_qualified_name":"set2","ident_utf16":{"start":{"line_number":108,"utf16_col":0},"end":{"line_number":108,"utf16_col":4}},"extent_utf16":{"start":{"line_number":108,"utf16_col":0},"end":{"line_number":108,"utf16_col":16}}},{"name":"set3","kind":"constant","ident_start":1565,"ident_end":1569,"extent_start":1565,"extent_end":1588,"fully_qualified_name":"set3","ident_utf16":{"start":{"line_number":110,"utf16_col":0},"end":{"line_number":110,"utf16_col":4}},"extent_utf16":{"start":{"line_number":110,"utf16_col":0},"end":{"line_number":110,"utf16_col":23}}},{"name":"set1","kind":"constant","ident_start":1607,"ident_end":1611,"extent_start":1607,"extent_end":1630,"fully_qualified_name":"set1","ident_utf16":{"start":{"line_number":114,"utf16_col":0},"end":{"line_number":114,"utf16_col":4}},"extent_utf16":{"start":{"line_number":114,"utf16_col":0},"end":{"line_number":114,"utf16_col":23}}},{"name":"set2","kind":"constant","ident_start":1632,"ident_end":1636,"extent_start":1632,"extent_end":1648,"fully_qualified_name":"set2","ident_utf16":{"start":{"line_number":115,"utf16_col":0},"end":{"line_number":115,"utf16_col":4}},"extent_utf16":{"start":{"line_number":115,"utf16_col":0},"end":{"line_number":115,"utf16_col":16}}},{"name":"x","kind":"constant","ident_start":1688,"ident_end":1689,"extent_start":1688,"extent_end":1721,"fully_qualified_name":"x","ident_utf16":{"start":{"line_number":121,"utf16_col":0},"end":{"line_number":121,"utf16_col":1}},"extent_utf16":{"start":{"line_number":121,"utf16_col":0},"end":{"line_number":121,"utf16_col":33}}},{"name":"y","kind":"constant","ident_start":1723,"ident_end":1724,"extent_start":1723,"extent_end":1759,"fully_qualified_name":"y","ident_utf16":{"start":{"line_number":122,"utf16_col":0},"end":{"line_number":122,"utf16_col":1}},"extent_utf16":{"start":{"line_number":122,"utf16_col":0},"end":{"line_number":122,"utf16_col":36}}},{"name":"x","kind":"constant","ident_start":1805,"ident_end":1806,"extent_start":1805,"extent_end":1838,"fully_qualified_name":"x","ident_utf16":{"start":{"line_number":129,"utf16_col":0},"end":{"line_number":129,"utf16_col":1}},"extent_utf16":{"start":{"line_number":129,"utf16_col":0},"end":{"line_number":129,"utf16_col":33}}},{"name":"y","kind":"constant","ident_start":1840,"ident_end":1841,"extent_start":1840,"extent_end":1876,"fully_qualified_name":"y","ident_utf16":{"start":{"line_number":130,"utf16_col":0},"end":{"line_number":130,"utf16_col":1}},"extent_utf16":{"start":{"line_number":130,"utf16_col":0},"end":{"line_number":130,"utf16_col":36}}},{"name":"z","kind":"constant","ident_start":1880,"ident_end":1881,"extent_start":1880,"extent_end":1901,"fully_qualified_name":"z","ident_utf16":{"start":{"line_number":132,"utf16_col":0},"end":{"line_number":132,"utf16_col":1}},"extent_utf16":{"start":{"line_number":132,"utf16_col":0},"end":{"line_number":132,"utf16_col":21}}},{"name":"x","kind":"constant","ident_start":1919,"ident_end":1920,"extent_start":1919,"extent_end":1952,"fully_qualified_name":"x","ident_utf16":{"start":{"line_number":137,"utf16_col":0},"end":{"line_number":137,"utf16_col":1}},"extent_utf16":{"start":{"line_number":137,"utf16_col":0},"end":{"line_number":137,"utf16_col":33}}},{"name":"y","kind":"constant","ident_start":1954,"ident_end":1955,"extent_start":1954,"extent_end":1990,"fully_qualified_name":"y","ident_utf16":{"start":{"line_number":138,"utf16_col":0},"end":{"line_number":138,"utf16_col":1}},"extent_utf16":{"start":{"line_number":138,"utf16_col":0},"end":{"line_number":138,"utf16_col":36}}},{"name":"x","kind":"constant","ident_start":2044,"ident_end":2045,"extent_start":2044,"extent_end":2077,"fully_qualified_name":"x","ident_utf16":{"start":{"line_number":145,"utf16_col":0},"end":{"line_number":145,"utf16_col":1}},"extent_utf16":{"start":{"line_number":145,"utf16_col":0},"end":{"line_number":145,"utf16_col":33}}},{"name":"y","kind":"constant","ident_start":2079,"ident_end":2080,"extent_start":2079,"extent_end":2115,"fully_qualified_name":"y","ident_utf16":{"start":{"line_number":146,"utf16_col":0},"end":{"line_number":146,"utf16_col":1}},"extent_utf16":{"start":{"line_number":146,"utf16_col":0},"end":{"line_number":146,"utf16_col":36}}},{"name":"z","kind":"constant","ident_start":2119,"ident_end":2120,"extent_start":2119,"extent_end":2148,"fully_qualified_name":"z","ident_utf16":{"start":{"line_number":148,"utf16_col":0},"end":{"line_number":148,"utf16_col":1}},"extent_utf16":{"start":{"line_number":148,"utf16_col":0},"end":{"line_number":148,"utf16_col":29}}}]}},"copilotInfo":{"documentationUrl":"https://docs.github.com/copilot/overview-of-github-copilot/about-github-copilot-for-individuals","notices":{"codeViewPopover":{"dismissed":false,"dismissPath":"/settings/dismiss-notice/code_view_copilot_popover"}},"userAccess":{"accessAllowed":false,"hasSubscriptionEnded":false,"orgHasCFBAccess":false,"userHasCFIAccess":false,"userHasOrgs":false,"userIsOrgAdmin":false,"userIsOrgMember":false,"business":null,"featureRequestInfo":null}},"copilotAccessAllowed":false,"csrf_tokens":{"/progermyn/pp2-22B031111/branches":{"post":"u6IBFJBG9eNJIMtbo17wXp-dfMZqQpijwbQNfuVid19WX54ugKGEV5vbKq2mLEUUWclDDBacEjOCjaLAT4P6Qw"},"/repos/preferences":{"post":"qrJVR4goTMO2MQoGM2j2tiI4Q2ThkKb1n94eHsA6HDW7bHZbCwQyb0sBbv5J1MC8dPwTO-3_q9wFtJe0z8Ujug"}}},"title":"pp2-22B031111/tsis2/6.py at main · progermyn/pp2-22B031111"}