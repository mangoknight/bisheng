# Router for base api
from bisheng.api.v1 import (chat_router, endpoints_router, flow_styles_router,
                            flows_router, knowledge_router, server_router,
                            skillcenter_router, user_router, validate_router)
from fastapi import APIRouter

router = APIRouter(
    prefix='/api/v1',
)
router.include_router(chat_router)
router.include_router(endpoints_router)
router.include_router(validate_router)
router.include_router(flows_router)
router.include_router(flow_styles_router)
router.include_router(skillcenter_router)
router.include_router(knowledge_router)
router.include_router(server_router)
router.include_router(user_router)
