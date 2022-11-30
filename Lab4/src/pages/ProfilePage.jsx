import {posts, users} from "../mocks";
import {Link, useParams} from "react-router-dom";
import {Post} from "../components/Post";

export const ProfilePage = () => {
    const {idUser} = useParams()
    const [user] = users.filter(user=>user.idUser === +idUser)

    return (
        <div className="w-full min-h-screen flex p-4">
            { !!user && (
                <div>
                    <p className="flex gap-1">
                        <Link to="/">Главная</Link>
                        /
                        <Link to={`/profile/${user.idUser}`}>{user.username}</Link>
                    </p>
                    <p className="text-2xl font-semibold">
                        {user.username}
                    </p>
                    <div className="flex gap-5">
                        {posts.map(post=> ( post.idUser === +idUser && <Post key={post.idPost} {...post}/>))}
                    </div>
                </div>)
            }
        </div>
    )
}