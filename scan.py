import os
import requests
import time

GITHUB_TOKEN = os.getenv('GH_PAT')
HEADERS = {'Authorization': f'token {GITHUB_TOKEN}'}
KEYWORDS = [
    "TalkscriptViewer",
    "copyModelCallFaqTemplateInfo",
    "getCallDetailDefaultModelData",
    "setTdCallActionLogLayout",
    "mergeCustomerAfterFunction",
    "updateCallKnowledgeInfoList",
    "contractorSearchListener",
    "fhAmiVoiceWebClientManager",
    "updateStaffLastReadActivityMsg",
    "stopCheckLatestSnsMessage",
    "createAgentAssistantSettingAvatar",
    "callbackAllAiSettingList",
    "SiteAgentAssistantSettingSlave",
    "RenkeiNaviKiban", "LinkNaviPlatform", "CUIAutomationControl", "NaviAccessibilityCUIA",
    "NaviAccessibilityCore", "NaviAccessbilityControl", "NaviContextEngine", "NaviCalculationEngineCore",
    "NaviCalculationEngineDefault", "NaviContextEngineCore", "NaviContextEngineDefault", "NaviGrpc",
    "NaviPlatform", "NaviPlatformStyles", "SmartPBXCuscon", "CDRTrafficReport", "KaianCreator",
    "com.ntt.smartpbx", "SoCoreNumberChange", "SoHenkouHenkou", "SoHenkouSakuzyo",
    "SoHenkouTsuika", "jp.co.ntt.marble", "esnossAlarm", "CssbAlarm", "scenarioFlowDef.bpmn",
    "scenarioStructDef.json", "resourceEdit.txt", "resourceEstimate.txt", "tool_orch_apl", "tool_apl_gen",
    "FluentdRedirect", "fluentd_redirect", "td-agent_cssb", "td-agent_esnoss", "td-agent_jupiter",
    "td-agent_nexas", "td-agent_sni", "MediatorAladin", "MediatorEpc", "MediatorFicMonitor",
    "MediatorFicSimGroupDbvGW", "MediatorFivegc", "MediatorFivegcMonitor", "MediatorFivegcRadius",
    "MediatorFivegcReleaseFip", "MediatorFivegcSimGroupDb", "MediatorFivegcSimGroupDbSim",
    "MediatorFivegcSimGroupDbVgw", "MediatorFpgaVgw", "MediatorGetResumeInfo", "MediatorMoBills",
    "MediatorOpenStackCP", "MediatorPh2Epc",
    "MediatorPh2ReleaseFip", "MediatorPh2SimGroupDb", "MediatorPh2SimGroupDbSim",
    "MediatorPh2SimGroupDbvGW", "MediatorRadius", "MediatorReleaseFip", "MediatorSimGroupDb",
    "MediatorSimGroupDbSim", "MediatorSimGroupDbvGW", "MediatorStoreDb", "MediatorTransferDb",
    "MediatorUeGroupDbVgw", "MediatorUsageStream", "MediatorVgw", "MediatorVMwareCreatePort",
    "5gccmdb", "simgroupdb", "5gcsimgroupdb", "ph2simgroupdb", "ph2credentialdb",
    "epcinfodb", "5gcinfodb", "ph2epcinfodb", "delete-vcube-session",
    "drillserver_application", "drillserver_batch", "drillserver_htmlconvert",
    "frontgw_deploycustomdomainlambda", "frontgw_maillambda", "frontgw_maillamdba_processsendmailresult",
    "frontgw_maillamdba_sendmail", "frontgw_reloadipadresseslamdba", "frontgw_sslloginlambda",
    "frontgw_videolamdba", "frontgw_videoupdatestatuslamdba", "newfront_management",
    "smartstudy-dev-frontend", "smartstudy-dev-python", "smst-puppeteer", "drill", "vcube.host.url",
    "external.muf.adminSiteUrl", "external.ss.apiUrl", "external.fcm.authKey", "external.gmo.baseUrl",
    "external.gmo.tokenScriptUrl", "external.fcm.baseUrl", "int_rounded_clipped_x",
    "PER_PAGE_MEDICAL_EXAMINATION_DETAIL", "deepprotect-tp", "deepprotect_tp", "IERAE_ID",
    "tpars-vision-ai", "tpars-analysis", "TPARSANALYSIS", "IDEA_YAML_FILE_PATH",
    "CORR_RAND_MT_COUNT_AT_ONCE_MAX", "test_largemem_corr_rand_gen_prand_u32",
    "clipped_int_rounded_clipped_x", "KARTE_RP_SUPPORT_EMAIL_ADDRESS", "KARTE_OIDC_RESPONSE_URL",
    "Deviation_LifeWorkBalanceClass_HarassmentClass", "pulse-devinf-python-psql",
    "FORMAT.PADICO_DATE_ZONE_FORMAT", "everysense.debug_address", "pt-meti-sns-itoki",
    "product-search-product-set-is-locked", "idea-stg-sns-triger-for-lambda",
    "service point", "supply-selling-service", "pricing-engine",
    "rapid-api", "billing-engine", "gemini-promotion", 
    "com.dhl.ecs.retail.ecwallet.function", "com.dp.authentication",
    "com.dp.retail", "com.dhl.esc.gemini", "com.dhl.pos", "com.dhl.ecpay",
    "Testcase 5.11_212", "LoginAndLogout.Logout FH", "${SERVER_IP}/fasthelp5",
    'SiteManagement.Check "Approval Flow Detail" SW Is Displayed by New Mode',
    "${KNOWLEDGE_MANAGEMENT_URL}", "Global_Navigation.Open Client Script List Screen From Global Navigation",
    "MyTicket_Supervisor.Check First Category Row Is Displayed On List After Set Multiple Category",
    "KN_Dashboard.Create Knowledge For Waiting Approval", "SideMenu_Navigation.Open New SMS Screen",
    "SupportGroupManagement.Close TalkScript Editor SW", "${URL_BASE}/CallManage.html",
    "rbxframework", "rbmstreaming", "rbmsession", "RbxFrameworx", "RbxfwxApplication", "Rbxbackpin",
    "RBXFWX_IMPROVE_MULTI_BPM_SYNC", "RBXFWX_BUILD_TYPE", 
    "RbxFrameworxHostAppConfig", "RbxFrameworx", "IDjControlClient", "RBXFAILSAFE_EXISTENCE_CHECK2", "RBXDBG_LOG_AND_BREAK",
    "seatmap-api-client", "seatmap-communication-client", "seatmap-data-eliminator",
    "seatmap-manual-amazon-connect", "seatmap-operator-client", "seatmap-provider-purecloud",
    "seatmap-provider-storm", "seatmap-setupper-amazon-connect", "seatmap-tenant-config-loader",
    "seatmap-tenant-user-loader", "dashboard-manual-amazon-connect",
    "dashboard-provider-amazon-connect", "dashboard-provider-purecloud", "dashboard-setupper-amazon-connect",
    "dashboard-tenant-config-loader", "dashboard-tenant-user-loader", 
    "com.icario.dhp", "data-health-platform", "dhp-segmentation-service", "dhp-personalization-service", "dhp-outreach-service",
    "dhp-program-service", "dhp-program-member-service", "dhp-member-service", "dhp-survey-service",
    "data-append-flag", "member-dnc", "member-next-action-group", 
    "sheet_parent_child_master_mapping_all", "sheet_product_group_header_mapping_all", "sheet_product_type_header_mapping_all", 
    "sheet_parent_child_header_mapping_all", "find_carton_left_side", "create_sheet_details_container_pack"
]
found = False

with open("scan-results.txt", "w", encoding="utf-8") as f:
    for keyword in KEYWORDS:
        url = f"https://api.github.com/search/code?q={keyword}+in:file"
        res = requests.get(url, headers=HEADERS)
        if res.status_code == 200:
            items = res.json().get("items", [])
            if items:
                found = True
            f.write(f"🔎 Keyword: {keyword} ({len(items)} hits)\n")
            for item in items:
                f.write(f"  → {item['html_url']}\n")
        time.sleep(2)

# Set output for GitHub Actions
with open(os.environ['GITHUB_OUTPUT'], 'a') as out:
    out.write(f"result_found={'true' if found else 'false'}\n")
