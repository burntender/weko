# .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp


from unittest.mock import MagicMock
import uuid
import pytest
import uuid
from mock import patch
from flask import Flask, json, jsonify, url_for, session, make_response
from invenio_accounts.testutils import login_user_via_session as login
from werkzeug.exceptions import InternalServerError ,NotFound,Forbidden
from weko_workflow.admin import FlowSettingView,WorkFlowSettingView
<<<<<<< HEAD
from weko_workflow.models import FlowDefine, FlowAction, FlowActionRole, WorkFlow, WorkflowRole

=======
from weko_workflow.models import FlowDefine, WorkFlow
>>>>>>> pr1362
# class FlowSettingView(BaseView):
class TestFlowSettingView:
# .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestFlowSettingView::test_index_acl_guest -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
#     def index(self):
    def test_index_acl_guest(self,client,db_register2):
        url = url_for('flowsetting.index',_external=True)
        res =  client.get(url)
        assert res.status_code == 302

    # .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestFlowSettingView::test_index_acl -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    @pytest.mark.parametrize('users_index, status_code', [
        (0, 403),
        # (1, 200),
        # (2, 200),
        # (3, 200),
        # (4, 200),
        # (5, 200),
        # (6, 200),
    ])
    def test_index_acl(self,client,db_register2,users,users_index,status_code):
        login(client=client, email=users[users_index]['email'])
        url = url_for('flowsetting.index',_external=True)
        res =  client.get(url)
        assert res.status_code == status_code  

#     def flow_detail(self, flow_id='0'):
# .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestFlowSettingView::test_flow_detail_acl_guest -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    def test_flow_detail_acl_guest(self,client,db_register2):
        url = url_for('flowsetting.index',flow_id=str(1),_external=True)
        res =  client.get(url)
        assert res.status_code == 302

    # .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestFlowSettingView::test_flow_detail_acl -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    @pytest.mark.parametrize('users_index, status_code', [
        # (0, 403),
        (1, 200),
        # (2, 200),
        # (3, 200),
        # (4, 200),
        # (5, 200),
        # (6, 200),
    ])
    def test_flow_detail_acl(self,client,workflow,db_register2,users,users_index,status_code):
        flow_define = workflow['flow']
        login(client=client, email=users[users_index]['email'])
<<<<<<< HEAD
        url = '/admin/flowsetting/{}'.format(0)
=======
        url = '/admin/workflowsetting/{}'.format(0)
        url = '/admin/flowsetting/{}'.format(0)
        print(url)
>>>>>>> pr1362
        with patch("flask.templating._render", return_value=""):
            res =  client.get(url)
            assert res.status_code == status_code
        
        
        url = '/admin/flowsetting/{}'.format(flow_define.flow_id)
        with patch("flask.templating._render", return_value=""):
            res =  client.get(url)
            assert res.status_code == status_code  

    # def flow_detail(self, flow_id='0'):
    # def new_flow(self, flow_id='0'):
    # def del_flow(self, flow_id='0'):
    # .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestFlowSettingView::test_flow_detail_update_delete -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    def test_flow_detail_update_delete(self,app,client,users,workflow ,workflow_open_restricted):
        #repoadmin
        login(client=client, email=users[1]['email'])
        url = '/admin/flowsetting/{}'.format(workflow_open_restricted[1]["flow"].flow_id)

        with patch("flask.templating._render", return_value=""):
            #104
            res =  client.get(url)
            assert res.status_code == 403
            #105
            res =  client.post(url)
            assert res.status_code == 403
            # 106
            res =  client.delete(url)
            assert res.status_code == 403

            url = '/admin/flowsetting/{}'.format("hoge")
            res =  client.get(url)
            assert res.status_code == 404
            
    
#     def get_specified_properties():
# .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestFlowSettingView::test_get_specified_properties -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    def test_get_specified_properties(self,app,item_type):
        with app.test_request_context():
            assert FlowSettingView.get_specified_properties()==[{'value': 'parentkey.subitem_restricted_access_guarantor_mail_address', 'text': 'Guarantor'}]
        
#     def update_flow(flow_id):
#     def new_flow(self, flow_id='0'):
# .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestFlowSettingView::test_new_flow -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
<<<<<<< HEAD
    def test_new_flow(self,app,client,action_data,users):
        login(client=client, email=users[1]['email'])
        url = '/admin/flowsetting/{}'.format(0)
        q = FlowDefine.query.all()
        assert len(q) == 0
        with patch("flask.templating._render", return_value=""):
            res =  client.post(url)
            assert res.status_code == 500
        q = FlowDefine.query.all()
        assert len(q) == 0

        data = {"flow": "test1"}
        login(client=client, email=users[1]['email'])
        url = '/admin/flowsetting/{}'.format(0)
        with patch("flask.templating._render", return_value=""):
            res =  client.post(url, data=json.dumps(data), headers=[('Content-Type', 'application/json')])
            assert res.status_code == 400
        q = FlowDefine.query.all()
        assert len(q) == 0

        data = {"flow_name": "test1"}
        login(client=client, email=users[1]['email'])
        url = '/admin/flowsetting/{}'.format(0)
        with patch("flask.templating._render", return_value=""):
            res =  client.post(url, data=json.dumps(data), headers=[('Content-Type', 'application/json')])
            assert res.status_code == 200
        q = FlowDefine.query.all()
        assert len(q) == 1

        data = {"flow_name": "test1"}
        login(client=client, email=users[1]['email'])
        url = '/admin/flowsetting/{}'.format(0)
        with patch("flask.templating._render", return_value=""):
            res =  client.post(url, data=json.dumps(data), headers=[('Content-Type', 'application/json')])
            assert res.status_code == 400
        q = FlowDefine.query.all()
        assert len(q) == 1

        flow_id = q[0].flow_id
        data = {"flow_name": "test2"}
        login(client=client, email=users[1]['email'])
        url = '/admin/flowsetting/{}'.format(flow_id)
        with patch("flask.templating._render", return_value=""):
            res =  client.post(url, data=json.dumps(data), headers=[('Content-Type', 'application/json')])
            assert res.status_code == 200
        q = FlowDefine.query.first()
        assert q.flow_name == 'test2'

        data = {"flow": "test3"}
        login(client=client, email=users[1]['email'])
        url = '/admin/flowsetting/{}'.format(flow_id)
        with patch("flask.templating._render", return_value=""):
            res =  client.post(url, data=json.dumps(data), headers=[('Content-Type', 'application/json')])
            assert res.status_code == 400
        q = FlowDefine.query.first()
        assert q.flow_name == 'test2'

        data = {"flow_name": "test1"}
        login(client=client, email=users[1]['email'])
        url = '/admin/flowsetting/{}'.format(0)
        with patch("flask.templating._render", return_value=""):
            res =  client.post(url, data=json.dumps(data), headers=[('Content-Type', 'application/json')])
            assert res.status_code == 200
        q = FlowDefine.query.all()
        assert len(q) == 2

        data = {"flow_name": "test1"}
        login(client=client, email=users[1]['email'])
        url = '/admin/flowsetting/{}'.format(flow_id)
        with patch("flask.templating._render", return_value=""):
            res =  client.post(url, data=json.dumps(data), headers=[('Content-Type', 'application/json')])
            assert res.status_code == 400
        q = FlowDefine.query.first()
        assert q.flow_name == 'test2'

        login(client=client, email=users[1]['email'])
        url = '/admin/flowsetting/{}'.format(flow_id)
        with patch("flask.templating._render", return_value=""):
            res =  client.post(url)
            assert res.status_code == 500
        q = FlowDefine.query.first()
        assert q.flow_name == 'test2'
=======
    def test_new_flow(self,app,workflow):
        with app.test_request_context( "/admin/workflowsetting/"+str(workflow["flow"].flow_id), method="POST",headers={"Content-Type": "application/json"} ,data='{"flow_name": "flow_name1"}'):
            with patch('weko_workflow.admin.FlowSettingView._check_auth',return_value=False):
                with pytest.raises(Forbidden):
                    FlowSettingView().new_flow(str(workflow["flow"].flow_id))
            with patch('weko_workflow.admin.FlowSettingView._check_auth',return_value=True):
                res = FlowSettingView().new_flow(str(workflow["flow"].flow_id))
                assert json.loads(res.data).get("code","") == 0
        with app.test_request_context( "/admin/workflowsetting/"+str(workflow["flow"].flow_id), method="POST",headers={"Content-Type": "application/json"} ,data='{"flow_name": "flow_name2"}'):
            res = FlowSettingView().new_flow("0")
            assert res.status_code == 200
            
            with patch('weko_workflow.admin.Flow.create_flow',side_effect=ValueError ):
                res = FlowSettingView().new_flow("0")
                assert res.status_code == 400
            
>>>>>>> pr1362

#     def del_flow(self, flow_id='0'):
# .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestFlowSettingView::test_del_flow -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    def test_del_flow(self,app,workflow):
        with app.test_request_context("/admin/workflowsetting/0", method="DELETE"):
            assert json.loads(FlowSettingView().del_flow("0").data).get("code","") == 500
        with app.test_request_context("/admin/workflowsetting/"+str(workflow["flow"].flow_id), method="DELETE"):
            with patch('weko_workflow.admin.FlowSettingView._check_auth',return_value=False):
                with pytest.raises(Forbidden):
                    FlowSettingView().del_flow(str(workflow["flow"].flow_id))
            with patch('weko_workflow.admin.FlowSettingView._check_auth',return_value=True):
                assert json.loads(FlowSettingView().del_flow(str(workflow["flow"].flow_id)).data).get("code","")  == 500
                with patch('weko_workflow.admin.Flow.get_flow_detail',return_value=""):
                    assert json.loads(FlowSettingView().del_flow(str(workflow["flow"].flow_id)).data).get("code","")  == 0
                with patch('weko_workflow.admin.WorkFlow.get_workflow_by_flow_id',return_value=[]):
                    assert json.loads(FlowSettingView().del_flow(str(workflow["flow"].flow_id)).data).get("code","")  == 500

#     def get_actions():
# .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestFlowSettingView::test_get_actions -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    def test_get_actions(self,app,workflow):
        with app.test_request_context():
            assert FlowSettingView.get_actions()==""
 
#     def upt_flow_action(self, flow_id=0):
<<<<<<< HEAD
# .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestFlowSettingView::test_upt_flow_action -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    def test_upt_flow_action(self,app,client,workflow,users):
        flow_define = workflow['flow']
        login(client=client, email=users[1]['email'])
        url = '/admin/flowsetting/action/{}'.format(flow_define.flow_id)
        q = FlowAction.query.filter_by(flow_id=flow_define.flow_id).all()
        assert len(q) == 7
        q = FlowActionRole.query.all()
        assert len(q) == 0
        with patch("flask.templating._render", return_value=""):
            res =  client.post(url)
            assert res.status_code == 400
        q = FlowAction.query.filter_by(flow_id=flow_define.flow_id).all()
        assert len(q) == 7

        data = [
            {
                "id":"5",
                "version":"1.0.1",
                "user":"0",
                "user_deny":False,
                "role":"0",
                "role_deny":False,
                "workflow_flow_action_id":3,
                "send_mail_setting":{
                    "request_approval":False,
                    "inform_approval":False,
                    "inform_reject":False
                }
                ,"action":"DEL"
            }
        ]
        with patch("flask.templating._render", return_value=""):
            res =  client.post(url, data=json.dumps(data), headers=[('Content-Type', 'application/json')])
            assert res.status_code == 200
        q = FlowAction.query.filter_by(flow_id=flow_define.flow_id).all()
        assert len(q) == 6

        q = FlowActionRole.query.all()
        assert len(q) == 0

        data = [
            {
                "id":"3",
                "version":"1.0.1",
                "user":"0",
                "user_deny":False,
                "role":"0",
                "role_deny":False,
                "workflow_flow_action_id":2,
                "send_mail_setting":{
                    "request_approval":False,
                    "inform_approval":False,
                    "inform_reject":False
                },
                "action":"ADD"
            },
            {
                "id":"5",
                "version":"1.0.1",
                "user":"contributor@test.org",
                "user_deny":False,
                "role":"0",
                "role_deny":False,
                "workflow_flow_action_id":3,
                "send_mail_setting":{
                    "request_approval":False,
                    "inform_approval":False,
                    "inform_reject":False
                }
                ,"action":"ADD"
            }
        ]
        with patch("flask.templating._render", return_value=""):
            res =  client.post(url, data=json.dumps(data), headers=[('Content-Type', 'application/json')])
            assert res.status_code == 200
        q = FlowAction.query.filter_by(flow_id=flow_define.flow_id).all()
        assert len(q) == 7
        q = FlowActionRole.query.all()
        assert len(q) == 1
=======
# .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestFlowSettingView::test_index_acl -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    def test_upt_flow_action(self,app,workflow):
        with app.test_request_context("/admin/workflowsetting/action/"+str(workflow["flow"].flow_id), method="POST",headers={"Content-Type": "application/json"} ,data='{"flow_name": "flow_name1"}'):
            with patch('weko_workflow.admin.FlowSettingView._check_auth',return_value=False):
                with pytest.raises(Forbidden):
                    assert FlowSettingView().upt_flow_action(str(workflow["flow"].flow_id))
            with patch('weko_workflow.admin.FlowSettingView._check_auth',return_value=True):
                with patch('weko_workflow.admin.Flow.upt_flow_action',return_value=True):
                    assert json.loads(FlowSettingView().upt_flow_action(str(workflow["flow"].flow_id)).data).get("code","")  == 0
            
# def _check_auth(flow_id:str ):
# .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestFlowSettingView::test__check_auth -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    def test__check_auth(self,app,users,workflow ,workflow_open_restricted):
        # 99
        assert FlowSettingView._check_auth('0')

        with app.test_request_context():
            # 100
            # sysadmin
            with patch('flask_login.utils._get_user',return_value=users[2]["obj"]):
                assert FlowSettingView._check_auth(workflow["flow"].flow_id)
            #repoadmin
            with patch('flask_login.utils._get_user',return_value=users[1]["obj"]):

                #101
                try:
                    FlowSettingView._check_auth(str(uuid.uuid4()))
                    assert False
                except InternalServerError as ex:
                    assert ex.code == 500
                
                #102
                assert FlowSettingView._check_auth(workflow["flow"].flow_id)
                #103
                assert not FlowSettingView._check_auth(workflow_open_restricted[1]["flow"].flow_id)
                
>>>>>>> pr1362

# class WorkFlowSettingView(BaseView):
# .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestWorkFlowSettingView -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
class TestWorkFlowSettingView:
    #     def index(self):
    # .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestWorkFlowSettingView::test_index_acl_guest -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    def test_index_acl_guest(self,client,db_register2):
        url = url_for('workflowsetting.index',_external=True)
        res =  client.get(url)
        assert res.status_code == 302

    # .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestWorkFlowSettingView::test_index_acl -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    @pytest.mark.parametrize('users_index, status_code', [
        # (0, 403),
        (1, 200),
        # (2, 200),
        # (3, 200),
        # (4, 200),
        # (5, 200),
        # (6, 200),
    ])
    def test_index_acl(self,client,db_register2,users,users_index,status_code):
        login(client=client, email=users[users_index]['email'])
        url = url_for('workflowsetting.index',_external=True)
        res =  client.get(url)
        assert res.status_code == status_code  

    #     def workflow_detail(self, workflow_id='0'):
    # .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestWorkFlowSettingView::test_workflow_detail_acl_guest -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    def test_workflow_detail_acl_guest(self,client,db_register2):
        url = url_for('workflowsetting.workflow_detail',workflow_id='0',_external=True)
        res =  client.get(url)
        assert res.status_code == 302

    # .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestWorkFlowSettingView::test_workflow_detail_acl -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    @pytest.mark.parametrize('users_index, status_code', [
        # (0, 403),
        (1, 200),
        (2, 200),
        # (3, 200),
        # (4, 200),
        # (5, 200),
        # (6, 200),
    ])
    def test_workflow_detail_acl(self,app ,client,db_register,workflow_open_restricted, db_register2,users,users_index,status_code,mocker):
        login(client=client, email=users[users_index]['email'])
        url = url_for('workflowsetting.workflow_detail',workflow_id='0',_external=True)
        mock_render =mocker.patch("flask.templating._render", return_value=make_response())
        res =  client.get(url)
        assert res.status_code == status_code  
        is_sysadmin = users_index == 2
        args, kwargs = mock_render.call_args
        # 81
        assert args[1]["is_sysadmin"] == is_sysadmin

        wf:WorkFlow = workflow_open_restricted[0]["workflow"]
        flows_id = wf.flows_id
        url = url_for('workflowsetting.workflow_detail',workflow_id=flows_id,_external=True)
        is_sysadmin = users_index == 2
        res =  client.get(url)
        args, kwargs = mock_render.call_args
        assert args[1]["is_sysadmin"] == is_sysadmin
        if not is_sysadmin:
            assert res.status_code == 403
        else:
            assert res.status_code == status_code

        #117
        wf:WorkFlow = db_register["workflow"]
        flows_id = wf.flows_id
        url = url_for('workflowsetting.workflow_detail',workflow_id=flows_id,_external=True)
        with patch('weko_workflow.admin.WEKO_WORKFLOW_SHOW_HARVESTING_ITEMS', False):
            res =  client.get(url)
            assert res.status_code == status_code

        

    #     def update_workflow(self, workflow_id='0'):
    # .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestWorkFlowSettingView::test_update_workflow_acl_guest -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    def test_update_workflow_acl_guest(self,client,db_register2):
        url = url_for('workflowsetting.update_workflow',workflow_id='0',_external=True)
        res =  client.post(url)
        assert res.status_code == 302
        
        res =  client.put(url)
        assert res.status_code == 302


    # .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestWorkFlowSettingView::test_update_workflow_acl -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    @pytest.mark.parametrize('users_index, status_code', [
        # (0, 403),
        (1, 200),
        # (2, 200),
        # (3, 200),
        # (4, 200),
        # (5, 200),
        # (6, 200),
    ])
    def test_update_workflow_acl(self,client,db_register2,workflow,users,users_index,status_code):
        login(client=client, email=users[users_index]['email'])
        url = '/admin/workflowsetting/{}'.format(0)
        q = WorkFlow.query.all()
        assert len(q) == 1
        with patch("flask.templating._render", return_value=""):
            with pytest.raises(AttributeError):
                res =  client.post(url)
        q = WorkFlow.query.all()
        assert len(q) == 1

        data = {
            "id": 1,
            "list_hide": {},
            "flows_name": "test",
            "itemtype_id": 1,
            "flow_id": 1,
            "index_id": None,
            "location_id": None,
            "open_restricted": True,
            "is_gakuninrdm": True
        }
        login(client=client, email=users[users_index]['email'])
        url = '/admin/workflowsetting/{}'.format(uuid.uuid4())
        with patch("flask.templating._render", return_value=""):
<<<<<<< HEAD
            res = client.post(url, data=json.dumps(data), headers=[('Content-Type', 'application/json')])
        assert res.status_code == 200

        q = WorkFlow.query.first()
        assert q.open_restricted == False
        assert q.is_gakuninrdm == False

        data = {
            "id": 1,
            "list_hide": [],
            "flows_name": "test",
            "itemtype_id": "test",
            "flow_id": 1,
            "index_id": None,
            "location_id": None,
            "open_restricted": True,
            "is_gakuninrdm": True
        }
        login(client=client, email=users[users_index]['email'])
        url = '/admin/workflowsetting/{}'.format(workflow['workflow'].flows_id)
        with patch("flask.templating._render", return_value=""):
            res = client.post(url, data=json.dumps(data), headers=[('Content-Type', 'application/json')])
        assert res.status_code == 400
        q = WorkFlow.query.first()
        assert q.open_restricted == False
        assert q.is_gakuninrdm == False

        q = WorkFlow.query.first()
        assert q.open_restricted == False
        assert q.is_gakuninrdm == False
        assert q.index_tree_id == None
        q = WorkflowRole.query.all()
        assert len(q) == 0
        data = {
            "id": 1,
            "list_hide": [4],
            "flows_name": "test",
            "itemtype_id": 1,
            "flow_id": 1,
            "index_id": 1,
            "location_id": None,
            "open_restricted": True,
            "is_gakuninrdm": True
        }
        login(client=client, email=users[users_index]['email'])
        url = '/admin/workflowsetting/{}'.format(workflow['workflow'].flows_id)
        with patch("flask.templating._render", return_value=""):
            res = client.post(url, data=json.dumps(data), headers=[('Content-Type', 'application/json')])
        assert res.status_code == 200
        q = WorkFlow.query.first()
        assert q.open_restricted == True
        assert q.is_gakuninrdm == True
        assert q.index_tree_id == 1
        q = WorkflowRole.query.all()
        assert len(q) == 1

        data = {
            "list_hide": [],
            "flows_name": "test",
            "itemtype_id": 1,
            "flow_id": 1,
            "index_id": None,
            "location_id": None,
            "open_restricted": False,
            "is_gakuninrdm": False
        }
        login(client=client, email=users[users_index]['email'])
        url = '/admin/workflowsetting/{}'.format(0)
        with patch("flask.templating._render", return_value=""):
            res = client.post(url, data=json.dumps(data), headers=[('Content-Type', 'application/json')])
        assert res.status_code == 200
        q = WorkFlow.query.all()
        assert len(q) == 2
=======
            res =  client.put(url)
            assert res.status_code == status_code  
    
    #     def update_workflow(self, workflow_id='0'):
    # .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestWorkFlowSettingView::test_update_workflow -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    def test_update_workflow(self,client,db,db_register2,users,workflow):
        login(client=client, email=users[1]['email'])
        define = workflow["flow"]
        wflow : WorkFlow = workflow["workflow"]
        url = url_for('workflowsetting.update_workflow',workflow_id=wflow.flows_id,_external=True)
        with patch("flask.templating._render", return_value=""):
            res =  client.post(url 
                                , headers=[('Content-Type', 'application/json')
                                            ,('Accept', 'application/json')]
                                , data=json.dumps({'id': wflow.id,'flow_id': define.id
                                                   })
                                )
            assert res.status_code == 200
            wf : WorkFlow = db.session.query(WorkFlow).filter_by(id = wflow.id).one_or_none()
            assert wf.open_restricted == False
            
            url = url_for('workflowsetting.update_workflow',workflow_id='0',_external=True)
            res =  client.post(url 
                                    , headers=[('Content-Type', 'application/json')
                                                ,('Accept', 'application/json')]
                                    , data=json.dumps({'id': wflow.id,'flow_id': define.id
                                                    ,'itemtype_id' :wflow.itemtype_id
                                                    ,'flows_id' : wflow.flows_id
                                                    ,'is_gakuninrdm' : False})
                                    )
>>>>>>> pr1362


    #  def delete_workflow(self, workflow_id='0'):
    # .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestWorkFlowSettingView::test_delete_workflow_acl_guest -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    def test_delete_workflow_acl_guest(self,client,db_register2):
        url = url_for('workflowsetting.delete_workflow',workflow_id='0',_external=True)
        res =  client.delete(url)
        assert res.status_code == 302

    # .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestWorkFlowSettingView::test_delete_workflow_acl -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    @pytest.mark.parametrize('users_index, status_code', [
        # (0, 403),
        (1, 200),
        # (2, 200),
        # (3, 200),
        # (4, 200),
        # (5, 200),
        # (6, 200),
    ])
    def test_delete_workflow_acl(self,client,db_register2,users,users_index,status_code):
        login(client=client, email=users[users_index]['email'])
        url = url_for('workflowsetting.delete_workflow',workflow_id='0',_external=True)
        with patch("flask.templating._render", return_value=""):
            res =  client.delete(url)
            assert res.status_code == status_code  

    # def get_name_display_hide(cls, list_hide, role):
    # .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestWorkFlowSettingView::test_get_name_display_hide -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    def test_get_name_display_hide(self,app,users):
        role0 = (users[0]['obj']).roles[0]
        role1 = (users[1]['obj']).roles[0]
        role2 = (users[2]['obj']).roles[0]
        role3 = (users[3]['obj']).roles[0]
        role4 = (users[4]['obj']).roles[0]
        
        with app.test_request_context():
            assert WorkFlowSettingView.get_name_display_hide([role0],[role0,role1,role2,role3,role4])==(['Repository Administrator', 'System Administrator', 'Community Administrator', 'General'], ['Contributor'])
         
    #  def get_displays(cls, list_hide, role):
    # .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestWorkFlowSettingView::test_get_displays -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    def test_get_displays(self,app,users):
        role0 = (users[0]['obj']).roles[0]
        role1 = (users[1]['obj']).roles[0]
        role2 = (users[2]['obj']).roles[0]
        role3 = (users[3]['obj']).roles[0]
        role4 = (users[4]['obj']).roles[0]
        
        with app.test_request_context():
            ret = WorkFlowSettingView.get_displays([role0],[role0,role1,role2,role3,role4])
            assert isinstance(ret,list)==True
            assert ret == [role1,role2,role3,role4]

    # def save_workflow_role(cls, wf_id, list_hide):
    # .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestWorkFlowSettingView::test_save_workflow_role -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    def test_save_workflow_role(self,app,users,workflow):
        role0 = (users[0]['obj']).roles[0]
        role1 = (users[1]['obj']).roles[0]
        role2 = (users[2]['obj']).roles[0]
        role3 = (users[3]['obj']).roles[0]
        role4 = (users[4]['obj']).roles[0]
        
        wf = workflow['workflow']
        
        with app.test_request_context():
            assert WorkFlowSettingView.save_workflow_role(wf.id,[role0.id,role1.id,role2.id,role3.id,role4.id])

    # def get_language_workflows(cls, key):
    # .tox/c1/bin/pytest --cov=weko_workflow tests/test_admin.py::TestWorkFlowSettingView::test_get_language_workflows -vv -s --cov-branch --cov-report=term --basetemp=/code/modules/weko-workflow/.tox/c1/tmp
    def test_get_language_workflows(self,users):
        with self.test_request_context():
            assert self.get_language_workflows("display")=="Display"
            assert WorkFlowSettingView.get_language_workflows("hide")=="Hide"
            assert WorkFlowSettingView.get_language_workflows("display_hide")=="Display/Hide"
            
        with self.test_request_context(headers=[("Accept-Language", "en")]):
            assert WorkFlowSettingView.get_language_workflows("display")=="Display"
            assert WorkFlowSettingView.get_language_workflows("hide")=="Hide"
            assert WorkFlowSettingView.get_language_workflows("display_hide")=="Display/Hide"
        
        with self.test_request_context(headers=[("Accept-Language", "ja")]):
            assert WorkFlowSettingView.get_language_workflows("display")=="表示"
            assert WorkFlowSettingView.get_language_workflows("hide")=="非表示"
            assert WorkFlowSettingView.get_language_workflows("display_hide")=="表示/非表示"
            

