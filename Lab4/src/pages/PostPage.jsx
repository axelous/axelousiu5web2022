import {Link, useParams} from "react-router-dom";
import {posts, users} from "../mocks";

export const PostPage = () => {
    const {idPost} = useParams()
    const [post] = posts.filter(post => post.idPost===+idPost)
    const [user] = users.filter(user=>user.idUser === post.idUser)

    return <div className="flex gap-4 p-4">
        <img src={post.photo} style={{height:"calc(100vh - 32px)"}} />
        <p className="self-start">
            <Link to={`/profile/${user.idUser}`} className="font-semibold" >{user.username}: </Link>
            {post.description}
        </p>
    </div>
}